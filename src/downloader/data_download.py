# Libraries to download
import yfinance as yf
import pandas as pd
import os
from datetime import datetime
from dataset import tickers2

# Configuration
start_date = "2023-08-01"
end_date = "2025-06-30"
interval = "1h"
output_dir = os.path.join("Data", f"data_{interval}")

# Create output folder if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Loop through each ticker
for ticker in tickers2:
    try:
        print(f"Downloading {ticker}...")
        data = yf.download(ticker, start=start_date, end=end_date, interval=interval, progress=False)

        if not data.empty:
            file_path = os.path.join(output_dir, f"{ticker}_{interval}_data.csv")
            data.to_csv(file_path)
            print(f"Saved {ticker} data to {file_path}")
        else:
            print(f"No data found for {ticker}")

    except Exception as e:
        print(f"Failed to download {ticker}: {e}")
