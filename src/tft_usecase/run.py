# run.py
"""
Simple runner script that handles everything
"""
import os
import sys
# from config import config

def check_data_directory():
    """Check if data directory exists and has files"""
    data_path = "Data/formatted_data_1h"
    if not os.path.exists(data_path):
        print(f"❌ Data directory not found: {data_path}")
        print("Please create the directory and add your CSV files.")
        return False
    
    csv_files = [f for f in os.listdir(data_path) if f.endswith('.csv')]
    if not csv_files:
        print(f"❌ No CSV files found in {data_path}")
        print("Please add your CSV files to this directory.")
        return False
    
    print(f"✅ Found {len(csv_files)} CSV files in {data_path}")
    return True

def run_training():
    """Run the training pipeline"""
    try:
        from main import main
        main()
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("Please run 'python setup.py' first to install dependencies.")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Training error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    print("🚀 TFT Forecasting Runner")
    print("=" * 50)
    
    if check_data_directory():
        print("Starting training pipeline...")
        run_training()
    else:
        print("Please fix the data directory issues and try again.")
