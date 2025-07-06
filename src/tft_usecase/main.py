# from data_preparation import load_and_merge_data
# from train_tft import create_datasets, train_model

# if __name__ == "__main__":
#     df = load_and_merge_data()
#     train_ds, val_ds = create_datasets(df)
#     model = train_model(train_ds, val_ds)


# main.py
import argparse
import sys
from pathlib import Path
from config import config
from data_preparation import DataPreprocessor,logger
from train_tft import TFTTrainer
from utils import ModelUtils


def main():
    """Main execution function"""
    parser = argparse.ArgumentParser(description='TFT Time Series Forecasting')
    parser.add_argument('--config', type=str, help='Path to config file')
    parser.add_argument('--epochs', type=int, default=10, help='Number of epochs')
    parser.add_argument('--batch_size', type=int, default=64, help='Batch size')
    parser.add_argument('--learning_rate', type=float, default=1e-3, help='Learning rate')
    
    args = parser.parse_args()
    
    # Update config with command line arguments
    if args.epochs:
        config.EPOCHS = args.epochs
    if args.batch_size:
        config.BATCH_SIZE = args.batch_size
    if args.learning_rate:
        config.LEARNING_RATE = args.learning_rate
    
    try:
        # Initialize components
        data_preprocessor = DataPreprocessor(config)
        tft_trainer = TFTTrainer(config)
        model_utils = ModelUtils(config)
        
        # Load and preprocess data
        logger.info("Loading and preprocessing data...")
        df = data_preprocessor.load_and_merge_data()
        
        # Create datasets
        logger.info("Creating datasets...")
        train_ds, val_ds = tft_trainer.create_datasets(df)
        
        # Train model
        logger.info("Training model...")
        model = tft_trainer.train_model(train_ds, val_ds)
        
        # Evaluate model
        logger.info("Evaluating model...")
        val_loader = val_ds.to_dataloader(train=False, batch_size=config.BATCH_SIZE)
        metrics = model_utils.evaluate_model(model, val_loader)
        
        # Plot results
        logger.info("Generating plots...")
        predictions = model.predict(val_loader)
        actuals = val_loader.dataset.y
        
        model_utils.plot_predictions(
            actuals.numpy().flatten(),
            predictions.numpy().flatten(),
            title="TFT Predictions vs Actual"
        )
        
        logger.info("Training completed successfully!")
        
    except Exception as e:
        logger.error(f"Error in main execution: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()