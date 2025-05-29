import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import os

# Set display options (optional for better debugging)
pd.set_option('display.max_columns', None)

# Directory where Excel files are stored
data_dir = 'data'

# List all Excel files in your directory
excel_files = [f for f in os.listdir(data_dir) if f.endswith('.xlsx') or f.endswith('.xls')]

# Dictionary to store all DataFrames
all_data = {}

for file in excel_files:
    file_path = os.path.join(data_dir, file)
    sheets = pd.read_excel(file_path, sheet_name=None)  # Load all sheets
    for sheet_name, df in sheets.items():
        key = f"{os.path.splitext(file)[0]}_{sheet_name}"  # Clean filename
        all_data[key] = df

def clean_data(df):
    # Example placeholder; update based on actual column names
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df = df.dropna(subset=['date'])  # Ensure all rows have dates
    df = df.drop_duplicates()
    return df

cleaned_data = {name: clean_data(df.copy()) for name, df in all_data.items()}

with pd.ExcelWriter('cleaned_combined.xlsx') as writer:
    for name, df in cleaned_data.items():
        df.to_excel(writer, sheet_name=name[:31])  # Sheet name max = 31 chars

# Initialize empty DataFrame
combined_df = pd.DataFrame()

# Loop through datasets and extract relevant columns
for name, df in cleaned_data.items():
    if {'date', 'weight', 'working sets', 'reps'}.issubset(df.columns):
        temp_df = df[['date', 'weight', 'working sets', 'reps']]
        temp_df['source'] = name  # Optional: track origin
        combined_df = pd.concat([combined_df, temp_df], ignore_index=True)

# Sort by date
combined_df = combined_df.sort_values('date')