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

# See unique teams and years
print(f"Unique Teams: {df['team'].nunique()}")
print(f"Years covered: {df['year'].min()} - {df['year'].max()}")
print(f"Register per year: {df.groupby('year').size().describe()}")

# Fill null values in ties column
df["ties"] = df["ties"].fillna(0).astype(int)

# Create a new column for win percentage
df["tot_games"] = (df["wins"] + df["losses"] + df["ties"])
df["win_pct"] = df["wins"] / df["tot_games"]

df["category"] = pd.cut(df["win_pct"], bins = [0, 0.3, 0.5, 0.7, 1], labels = ["Poor", "Average", "Good", "Excellent"])

#print(df[["team","year","win_pct","category"]].head())

var = ['wins','win_pct', 'points', 'points_opp','points_diff','total_yards','pass_yds','rush_yds','turnovers','pass_td','rush_td']

resume = df[var].describe().T
resume['rango'] = resume['max'] - resume['min']
resume['cv%'] = (resume['std'] / resume['mean'] * 100).round(1)  # coeficiente de variación
print(resume[['mean','std','min','50%','max','rango','cv%']].round(2))
