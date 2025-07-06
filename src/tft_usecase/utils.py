# import matplotlib.pyplot as plt

# def plot_predictions(actual, predicted, title="Predictions"):
#     plt.figure(figsize=(12, 6))
#     plt.plot(actual, label="Actual")
#     plt.plot(predicted, label="Predicted")
#     plt.legend()
#     plt.title(title)
#     plt.grid(True)
#     plt.show()

# utils.py
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from typing import Optional, List
import torch
from pytorch_forecasting import TimeSeriesDataSet
from data_preparation import logger
class ModelUtils:
    def __init__(self, config):
        self.config = config
    
    def plot_predictions(self, actual: np.ndarray, predicted: np.ndarray, 
                        title: str = "Predictions", save_path: Optional[str] = None):
        """Plot actual vs predicted values"""
        plt.figure(figsize=(15, 8))
        plt.plot(actual, label='Actual', alpha=0.7)
        plt.plot(predicted, label='Predicted', alpha=0.7)
        plt.legend()
        plt.title(title)
        plt.xlabel('Time')
        plt.ylabel('Price')
        plt.grid(True, alpha=0.3)
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()
    
    def plot_feature_importance(self, model, save_path: Optional[str] = None):
        """Plot feature importance from the model"""
        try:
            interpretation = model.interpret_output(model.predict(model.training.dataset))
            
            # Plot attention weights
            fig, axes = plt.subplots(2, 2, figsize=(15, 10))
            
            # Variable importance
            if hasattr(interpretation, 'feature_importances'):
                importance = interpretation.feature_importances
                axes[0, 0].barh(range(len(importance)), importance)
                axes[0, 0].set_title('Feature Importance')
                axes[0, 0].set_xlabel('Importance')
            
            # Attention weights
            if hasattr(interpretation, 'attention'):
                attention = interpretation.attention.mean(0).mean(0)
                axes[0, 1].plot(attention)
                axes[0, 1].set_title('Attention Weights')
                axes[0, 1].set_xlabel('Time Step')
            
            plt.tight_layout()
            
            if save_path:
                plt.savefig(save_path, dpi=300, bbox_inches='tight')
            plt.show()
            
        except Exception as e:
            logger.error(f"Error plotting feature importance: {str(e)}")
    
    def evaluate_model(self, model, val_loader):
        """Evaluate model performance"""
        try:
            predictions = model.predict(val_loader)
            
            # Calculate metrics
            mae = torch.nn.functional.l1_loss(predictions, val_loader.dataset.y)
            mse = torch.nn.functional.mse_loss(predictions, val_loader.dataset.y)
            rmse = torch.sqrt(mse)
            
            print(f"MAE: {mae:.4f}")
            print(f"MSE: {mse:.4f}")
            print(f"RMSE: {rmse:.4f}")
            
            return {
                'mae': mae.item(),
                'mse': mse.item(),
                'rmse': rmse.item()
            }
            
        except Exception as e:
            logger.error(f"Error evaluating model: {str(e)}")
            return {}
