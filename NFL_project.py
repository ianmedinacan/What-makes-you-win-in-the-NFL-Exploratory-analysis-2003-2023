import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv("C:\\Users\\ianme\\Desktop\\NFL_Project\\team_stats_2003_2023.csv")

# See data types and null values
print(df.info())
print("\n--- Null values ---")
print(df.isnull().sum()[df.isnull().sum() > 0])

# See duplicates
print(f"\nDuplicados: {df.duplicated().sum()}")

print(f"Unique Teams: {df['team'].nunique()}")
print(f"Years covered: {df['year'].min()} - {df['year'].max()}")
print(f"Register per year: {df.groupby('year').size().describe()}")