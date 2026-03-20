import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv("C:\\Users\\ianme\\Desktop\\NFL_Project\\team_stats_2003_2023.csv")

print(df.info())
