import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# List all Excel files in your directory
excel_files = [f for f in os.listdir() if f.endswith('.xlsx') or f.endswith('.xls')]

# Dictionary to store all DataFrames
all_data = {}

for file in excel_files:
    # Read all sheets from each file
    sheets = pd.read_excel(file, sheet_name=None)
    
    # Store with filename prefix for clarity
    for sheet_name, df in sheets.items():
        all_data[f"{file[:-5]}_{sheet_name}"] = df  # Removes .xlsx extension

print(f"Loaded {len(all_data)} tables from {len(excel_files)} files")

#q1_revenue = all_data['sales_Q1_Revenue']  # Access DataFrame

metcon = all_data['UserId3017457_Metcon_250506.xlsx']
gymnastics = all_data['UserId3017457_Gymnastics_250506.xlsx']
pRS = all_data['UserId3017457_PRs_250506.xlsx']
weightlifting = all_data['UserId3017457_Weightlifting_250506.xlsx']
weightliftingTotal = all_data['UserId3017457_WeightliftingTotal_250506.xlsx']

sheets = pd.read_excel(metcon, gymnastics, pRS, weightlifting, weightliftingTotal, sheet_name=None)  # Reads all sheets

# processing workflow
def clean_data(df):
    #Generic cleaning function template
    # 1. Handle missing values
    df = df.dropna(subset=['key_column'])
    
    # 2. Standardize formats
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    
    # 3. Remove duplicates
    return df.drop_duplicates()

# Apply cleaning to all tables
cleaned_data = {name: clean_data(df) for name, df in all_data.items()}

# Load all Excel sheets into a dictionary of DataFrames
#file_path = "your_data.xlsx"
#sheets = pd.read_excel(file_path, sheet_name=None)  # Reads all sheets

print(f"Loaded sheets: {list(sheets.keys())}")
# 1. Load Data
# df1 = pd.read_csv('Stress_Level_v1.csv')
# df2 = pd.read.csv('Stress_Level_v2.csv')

# 2. Basic Scatterplot
plt.figure(figsize=(10, 6))
plt.scatter(
    x=df['column_x'], 
    y=df['column_y'],
    alpha=0.5  # Transparency for overlapping points
)
plt.title('Relationship Between X and Y')
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.savefig('outputs/plots/basic_scatter.png')
plt.close()

# 2. Enhanced Scatterplot (with Seaborn)
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=df,
    x='column_x',
    y='column_y',
    hue='category_column',  # Color by a third variable
    size='size_column',     # Optional: Vary point sizes
    palette='viridis'       # Color scheme
)
plt.title('Enhanced Scatterplot')
plt.savefig('outputs/plots/seaborn_scatter.png')
plt.close()
