# import torch
# import pytorch_lightning as pl
# # from pytorch_forecasting import TimeSeriesDataSet, TemporalFusionTransformer, Baseline, Trainer
# from pytorch_forecasting import TimeSeriesDataSet, TemporalFusionTransformer, Baseline
# from pytorch_lightning import Trainer

# from pytorch_forecasting.metrics import SMAPE
# from pytorch_lightning.callbacks.early_stopping import EarlyStopping
# from pytorch_lightning.callbacks import LearningRateMonitor
# from pytorch_lightning.loggers import TensorBoardLogger
# from config import *
# from pytorch_forecasting.data import GroupNormalizer

# def create_datasets(df):
#     df["time_idx"] = df.groupby("Ticker_ID").cumcount()
#     df["Ticker_ID"] = df["Ticker_ID"].astype(str)  # or "category"
#     df = df[df['time_idx'] > SEQ_LENGTH + PRED_LENGTH]


#     training = TimeSeriesDataSet(
#         df[lambda x: x.time_idx < df.time_idx.max() * 0.8],
#         time_idx="time_idx",
#         target="Close",
#         group_ids=["Ticker_ID"],
#         max_encoder_length=SEQ_LENGTH,
#         max_prediction_length=PRED_LENGTH,
#         static_categoricals=["Ticker_ID"],
#         time_varying_known_reals=["time_idx", "hour", "weekday"],
#         time_varying_unknown_reals=["Close", "Open", "High", "Low", "Volume", "rsi", "macd", "ema_12", "ema_26", "atr", "adx"],
#         target_normalizer=GroupNormalizer(groups=["Ticker_ID"]),
#     )


#     validation = TimeSeriesDataSet.from_dataset(training, df, predict=True, stop_randomization=True)
#     return training, validation

# def train_model(training, validation):
#     train_loader = training.to_dataloader(train=True, batch_size=BATCH_SIZE)
#     val_loader = validation.to_dataloader(train=False, batch_size=BATCH_SIZE)

#     model = TemporalFusionTransformer.from_dataset(
#         training,
#         learning_rate=LEARNING_RATE,
#         hidden_size=32,
#         attention_head_size=4,
#         dropout=0.1,
#         loss=SMAPE(),
#         log_interval=10,
#         reduce_on_plateau_patience=4
#     )

#     trainer = pl.Trainer(
#         max_epochs=EPOCHS,
#         accelerator="auto",
#         callbacks=[EarlyStopping(monitor="val_loss", patience=5), LearningRateMonitor()],
#         logger=TensorBoardLogger("lightning_logs")
#     )

#     trainer.fit(model, train_loader, val_loader)
#     return model

# train_tft.py
import torch
import pytorch_lightning as pl
import pandas as pd 
from data_preparation import logger
from pytorch_forecasting import TimeSeriesDataSet, TemporalFusionTransformer
from pytorch_forecasting.metrics import SMAPE, MAE, MAPE
from pytorch_lightning.callbacks.early_stopping import EarlyStopping
from pytorch_lightning.callbacks import LearningRateMonitor, ModelCheckpoint
from pytorch_lightning.loggers import TensorBoardLogger
from pytorch_forecasting.data import GroupNormalizer
from typing import Tuple
import os

class TFTTrainer:
    def __init__(self, config):
        self.config = config
        
    def create_datasets(self, df: pd.DataFrame) -> Tuple[TimeSeriesDataSet, TimeSeriesDataSet]:
        """Create training and validation datasets"""
        try:
            # Ensure proper data types
            df['Ticker_ID'] = df['Ticker_ID'].astype(str)
            df = df[df['time_idx'] >= self.config.SEQ_LENGTH].copy()
            
            # Define the split point
            max_time_idx = df['time_idx'].max()
            train_cutoff = int(max_time_idx * self.config.TRAIN_SPLIT)
            
            # Create training dataset
            training = TimeSeriesDataSet(
                df[df['time_idx'] <= train_cutoff],
                time_idx='time_idx',
                target='Close',
                group_ids=['Ticker_ID'],
                max_encoder_length=self.config.SEQ_LENGTH,
                max_prediction_length=self.config.PRED_LENGTH,
                
                # Static features
                static_categoricals=['Ticker_ID'],
                
                # Time-varying known features (known in future)
                time_varying_known_reals=[
                    'time_idx', 'hour', 'weekday', 'day_of_month', 'month'
                ],
                
                # Time-varying unknown features (not known in future)
                time_varying_unknown_reals=[
                    'Close', 'Open', 'High', 'Low', 'Volume',
                    'price_change', 'high_low_ratio', 'volume_change',
                    'rsi', 'bb_high', 'bb_low', 'bb_mid', 'bb_width',
                    'macd', 'macd_signal', 'macd_hist',
                    'ema_12', 'ema_26', 'sma_20',
                    'atr', 'volatility', 'adx'
                ],
                
                # Normalization
                target_normalizer=GroupNormalizer(groups=['Ticker_ID']),
                
                # Additional parameters
                min_encoder_length=self.config.SEQ_LENGTH // 2,
                allow_missing_timesteps=True,
                add_relative_time_idx=True,
                add_target_scales=True,
                add_encoder_length=True,
            )
            
            # Create validation dataset
            validation = TimeSeriesDataSet.from_dataset(
                training, 
                df, 
                predict=True, 
                stop_randomization=True
            )
            
            logger.info(f"Training dataset size: {len(training)}")
            logger.info(f"Validation dataset size: {len(validation)}")
            
            return training, validation
            
        except Exception as e:
            logger.error(f"Error creating datasets: {str(e)}")
            raise
    
    def train_model(self, training: TimeSeriesDataSet, validation: TimeSeriesDataSet) -> TemporalFusionTransformer:
        """Train the TFT model"""
        try:
            # Create data loaders
            train_loader = training.to_dataloader(
                train=True, 
                batch_size=self.config.BATCH_SIZE,
                num_workers=0  # Set to 0 to avoid multiprocessing issues
            )
            val_loader = validation.to_dataloader(
                train=False, 
                batch_size=self.config.BATCH_SIZE * 2,
                num_workers=0
            )
            
            # Create model
            model = TemporalFusionTransformer.from_dataset(
                training,
                learning_rate=self.config.LEARNING_RATE,
                hidden_size=self.config.HIDDEN_SIZE,
                attention_head_size=self.config.ATTENTION_HEAD_SIZE,
                dropout=self.config.DROPOUT,
                hidden_continuous_size=self.config.HIDDEN_SIZE,
                loss=SMAPE(),
                log_interval=10,
                reduce_on_plateau_patience=self.config.REDUCE_LR_PATIENCE,
                optimizer='AdamW'
            )
            
            # Setup callbacks
            callbacks = [
                EarlyStopping(
                    monitor='val_loss',
                    patience=self.config.EARLY_STOPPING_PATIENCE,
                    verbose=True,
                    mode='min'
                ),
                LearningRateMonitor(),
                ModelCheckpoint(
                    dirpath=self.config.MODEL_SAVE_PATH,
                    filename='best_model',
                    monitor='val_loss',
                    mode='min',
                    save_top_k=1
                )
            ]
            
            # Setup logger
            logger_tb = TensorBoardLogger(
                save_dir=self.config.LOG_PATH,
                name='tft_model'
            )
            
            # Create trainer
            trainer = pl.Trainer(
                max_epochs=self.config.EPOCHS,
                accelerator='auto',
                devices='auto',
                callbacks=callbacks,
                logger=logger_tb,
                enable_checkpointing=True,
                enable_progress_bar=True,
                gradient_clip_val=0.1
            )
            
            # Train model
            logger.info("Starting training...")
            trainer.fit(model, train_loader, val_loader)
            
            logger.info("Training completed!")
            return model
            
        except Exception as e:
            logger.error(f"Error training model: {str(e)}")
            raise
