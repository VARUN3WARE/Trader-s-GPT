# setup.py
"""
Setup script for easy installation
"""
import subprocess
import sys
import os

def install_requirements():
    """Install required packages"""
    requirements = [
        "torch>=1.13.0",
        "pytorch-lightning>=1.8.0", 
        "pytorch-forecasting>=0.10.0",
        "pandas>=1.5.0",
        "numpy>=1.21.0",
        "scikit-learn>=1.1.0",
        "ta>=0.10.0",
        "matplotlib>=3.5.0",
        "tensorboard>=2.8.0",
        "plotly>=5.0.0"
    ]
    
    for requirement in requirements:
        print(f"Installing {requirement}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", requirement])

def create_directories():
    """Create necessary directories"""
    dirs = ["models", "logs", "Data", "Data/formatted_data_1h"]
    for dir_name in dirs:
        os.makedirs(dir_name, exist_ok=True)
        print(f"Created directory: {dir_name}")

if __name__ == "__main__":
    print("Setting up TFT Forecasting environment...")
    install_requirements()
    create_directories()
    print("Setup complete!")
