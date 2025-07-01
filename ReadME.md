# TradeGPT - Time Series Transformer for Stock Price Prediction

## Overview

TradeGPT is a PyTorch-based project implementing a Transformer model for forecasting stock price movements using historical 1-hour interval stock data. The model uses technical indicators and time-series data to predict future closing prices.

## Features

- Loads and preprocesses 1-hour stock data CSV files.
- Computes popular technical indicators (e.g., RSI, MACD, Bollinger Bands).
- Uses a Transformer architecture tailored for time series forecasting.
- Supports training, validation, and testing dataset splits.
- Sequential data handling without shuffling for time series consistency.
- Scales features using MinMaxScaler.
- Evaluation with plotting of predicted vs actual prices.
- Designed to run efficiently on local PCs, with GPU support if available.

## Requirements

- Python 3.8+
- PyTorch
- Pandas
- NumPy
- Scikit-learn
- Matplotlib

You can install the dependencies with:

```bash
pip install -r requirements.txt
```

## Usage

### Data Preparation

Place your 1-hour interval stock CSV files in the Output/formatted_data_1h/ directory.

### Training

The training script will sequentially train the model on each dataset in the folder, saving models and displaying loss progress.

### Evaluation

After training, models are evaluated on the test split and the prediction results are plotted for analysis.

### GPU Support

The code automatically detects and uses GPU if available for faster training.

## File Structure

```
.
├── Output/
│   └── formatted_data_1h/      # Folder for input stock CSV files
├── models/                     # Saved trained models (optional)
├── notebooks/                  # Jupyter notebooks (if any)
├── src/                    # Python scripts
├── .gitignore
├── README.md
└── requirements.txt
```
