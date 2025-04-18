import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. Load Data
df1 = pd.read_csv('Stress_Level_v1.csv')
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
