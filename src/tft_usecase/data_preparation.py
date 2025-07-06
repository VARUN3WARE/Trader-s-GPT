# data_preparation.py
import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import ta
from typing import List, Tuple, Optional
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataPreprocessor:
    def __init__(self, config):
        self.config = config
        self.ticker2id = {}
        self.scaler = MinMaxScaler()
        
    def load_and_merge_data(self) -> pd.DataFrame:
        """Load and merge all CSV files from the data directory"""
        try:
            csv_files = self._get_csv_files()
            if not csv_files:
                raise ValueError(f"No CSV files found in {self.config.DATA_PATH}")
            
            logger.info(f"Found {len(csv_files)} CSV files")
            
            # Create ticker to ID mapping
            self.ticker2id = {self._extract_ticker(f): i for i, f in enumerate(csv_files)}
            
            all_dfs = []
            for file_path in csv_files:
                df = self._load_single_file(file_path)
                if df is not None:
                    all_dfs.append(df)
            
            if not all_dfs:
                raise ValueError("No valid data files were loaded")
            
            merged_df = pd.concat(all_dfs, ignore_index=True)
            logger.info(f"Merged dataframe shape: {merged_df.shape}")
            
            return self._final_preprocessing(merged_df)
            
        except Exception as e:
            logger.error(f"Error in load_and_merge_data: {str(e)}")
            raise
    
    def _get_csv_files(self) -> List[str]:
        """Get all CSV files from the data directory"""
        if not os.path.exists(self.config.DATA_PATH):
            raise ValueError(f"Data path does not exist: {self.config.DATA_PATH}")
        
        return [
            os.path.join(self.config.DATA_PATH, f) 
            for f in os.listdir(self.config.DATA_PATH) 
            if f.endswith('.csv')
        ]
    
    def _extract_ticker(self, file_path: str) -> str:
        """Extract ticker symbol from filename"""
        return os.path.basename(file_path).split('_')[0]
    
    def _load_single_file(self, file_path: str) -> Optional[pd.DataFrame]:
        """Load and preprocess a single CSV file"""
        try:
            df = pd.read_csv(file_path, delimiter='\t')
            df.columns = df.columns.str.strip()
            
            # Parse datetime
            df['Gmt time'] = pd.to_datetime(df['Gmt time'], format='%d.%m.%Y %H:%M:%S.%f')
            df.sort_values('Gmt time', inplace=True)
            
            # Add ticker information
            ticker = self._extract_ticker(file_path)
            df['Ticker'] = ticker
            df['Ticker_ID'] = self.ticker2id[ticker]
            
            # Add features
            df = self._add_features(df)
            
            logger.info(f"Loaded {ticker}: {len(df)} rows")
            return df
            
        except Exception as e:
            logger.error(f"Error loading {file_path}: {str(e)}")
            return None
    
    def _add_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """Add technical indicators and time features"""
        try:
            # Time features
            df['hour'] = df['Gmt time'].dt.hour
            df['weekday'] = df['Gmt time'].dt.weekday
            df['day_of_month'] = df['Gmt time'].dt.day
            df['month'] = df['Gmt time'].dt.month
            
            # Price features
            df['price_change'] = df['Close'].pct_change()
            df['high_low_ratio'] = df['High'] / df['Low']
            df['volume_change'] = df['Volume'].pct_change()
            
            # Technical indicators
            df['rsi'] = ta.momentum.rsi(df['Close'], window=self.config.RSI_WINDOW)
            
            # Bollinger Bands
            bb = ta.volatility.BollingerBands(df['Close'])
            df['bb_high'] = bb.bollinger_hband()
            df['bb_low'] = bb.bollinger_lband()
            df['bb_mid'] = bb.bollinger_mavg()
            df['bb_width'] = (df['bb_high'] - df['bb_low']) / df['bb_mid']
            
            # MACD
            df['macd'] = ta.trend.macd_diff(df['Close'])
            df['macd_signal'] = ta.trend.macd_signal(df['Close'])
            df['macd_hist'] = ta.trend.macd(df['Close'])
            
            # Moving averages
            df['ema_12'] = ta.trend.ema_indicator(df['Close'], window=self.config.EMA_FAST)
            df['ema_26'] = ta.trend.ema_indicator(df['Close'], window=self.config.EMA_SLOW)
            df['sma_20'] = ta.trend.sma_indicator(df['Close'], window=20)
            
            # Volatility
            df['atr'] = ta.volatility.average_true_range(df['High'], df['Low'], df['Close'])
            df['volatility'] = df['Close'].rolling(window=20).std()
            
            # Trend
            df['adx'] = ta.trend.adx(df['High'], df['Low'], df['Close'])
            
            # Handle missing values
            df = df.bfill().ffill()
            
            # Remove rows with insufficient data
            df = df.iloc[max(self.config.RSI_WINDOW, self.config.EMA_SLOW, 20):]
            
            return df
            
        except Exception as e:
            logger.error(f"Error adding features: {str(e)}")
            return df
    
    def _final_preprocessing(self, df: pd.DataFrame) -> pd.DataFrame:
        """Final preprocessing steps"""
        # Remove any remaining NaN values
        df = df.dropna()
        
        # Sort by ticker and time
        df = df.sort_values(['Ticker_ID', 'Gmt time']).reset_index(drop=True)
        
        # Add time index for each ticker
        df['time_idx'] = df.groupby('Ticker_ID').cumcount()
        
        # Filter out insufficient data
        min_length = self.config.SEQ_LENGTH + self.config.PRED_LENGTH + 10
        ticker_counts = df.groupby('Ticker_ID').size()
        valid_tickers = ticker_counts[ticker_counts >= min_length].index
        df = df[df['Ticker_ID'].isin(valid_tickers)]
        
        logger.info(f"Final dataset shape: {df.shape}")
        logger.info(f"Valid tickers: {len(valid_tickers)}")
        
        return df
