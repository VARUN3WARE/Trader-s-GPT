# DATA_PATH = "Data/formatted_data_1h"
# SEQ_LENGTH = 60
# PRED_LENGTH = 1
# BATCH_SIZE = 64
# EPOCHS = 1
# LEARNING_RATE = 1e-3

# config.py
import os
from dataclasses import dataclass
from typing import Optional

@dataclass
class Config:
    # Data paths
    DATA_PATH: str = "Data/formatted_data_1h"
    MODEL_SAVE_PATH: str = "models"
    LOG_PATH: str = "logs"
    
    # Model parameters
    SEQ_LENGTH: int = 60
    PRED_LENGTH: int = 1
    BATCH_SIZE: int = 64
    EPOCHS: int = 10
    LEARNING_RATE: float = 1e-3
    
    # TFT specific parameters
    HIDDEN_SIZE: int = 32
    ATTENTION_HEAD_SIZE: int = 4
    DROPOUT: float = 0.1
    
    # Training parameters
    EARLY_STOPPING_PATIENCE: int = 5
    REDUCE_LR_PATIENCE: int = 4
    TRAIN_SPLIT: float = 0.8
    VAL_SPLIT: float = 0.1
    
    # Technical indicators
    RSI_WINDOW: int = 14
    EMA_FAST: int = 12
    EMA_SLOW: int = 26
    
    def __post_init__(self):
        # Create directories if they don't exist
        os.makedirs(self.MODEL_SAVE_PATH, exist_ok=True)
        os.makedirs(self.LOG_PATH, exist_ok=True)

# Initialize config
config = Config()