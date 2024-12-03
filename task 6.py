import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Movies.csv')
print(df.head())
print()

print(df.shape)
print()

df = df.drop_duplicates()
print(df.shape)
print()

print(df.describe())
print()

print(df.info())
print()


