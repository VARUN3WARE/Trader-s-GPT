import pandas as pd
import os
from glob import glob

# Set paths
input_dir = os.path.join("Output", "data_1h")
output_dir = os.path.join("Output", "formatted_data_1h")
os.makedirs(output_dir, exist_ok=True)

# Process all CSV files in input_dir
for file_path in glob(os.path.join(input_dir, "*.csv")):
    try:
        # Read CSV skipping the metadata rows
        df = pd.read_csv(file_path, skiprows=2)

        # Rename unnamed columns (fallback if headers are messy)
        df = df.rename(columns={
            'Datetime': 'Gmt time',
            'Price': 'Close',  # in case it's still used
            'Unnamed: 1': 'Close',
            'Unnamed: 2': 'High',
            'Unnamed: 3': 'Low',
            'Unnamed: 4': 'Open',
            'Unnamed: 5': 'Volume'
        })

        # Format datetime
        df['Gmt time'] = pd.to_datetime(df['Gmt time']).dt.strftime('%d.%m.%Y %H:%M:%S.000')

        # Reorder columns
        df = df[['Gmt time', 'Open', 'High', 'Low', 'Close', 'Volume']]

        # Round values for cleaner output
        df = df.round({'Open': 5, 'High': 5, 'Low': 5, 'Close': 5, 'Volume': 2})

        # Save to new folder (tab-separated)
        filename = os.path.basename(file_path)
        output_path = os.path.join(output_dir, filename)
        df.to_csv(output_path, index=False, sep='\t')

        print(f"✔ Converted: {filename}")

    except Exception as e:
        print(f"❌ Failed to process {file_path}: {e}")
