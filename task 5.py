import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('heart.csv')
print(df.head())
print()

print(df.tail())
print()

print(df.columns.values)
print()

print(df.isna().sum())
print()

print(df.info())
print()

df.hist(bins = 50, grid = False, figsize = (20,15));

print(df.describe())
print()

print("questions = ")
print("1. How many people have heart disease and how many people doesn't have heart disease")
print("2. People of which sex has most heart disease?")
print( "3. People of which sex has which type of chest pain most?")
print("4. People with which chest pain are most prone to have heart disease?")

print(df.target.value_counts())
print()
df.target.value_counts().plot(kind = 'bar',color = ["orchid","salmon"])
plt.title("Heart disease values")
plt.xlabel("1 = Heart Disese, 0 = No Heart disease")
plt.ylabel("Amount");

df.target.value_counts().plot(kind = 'pie', figsize = (8,6))
plt.legend(["Disease","No Disease"]);

print(df.sex.value_counts())
print()
df.sex.value_counts().plot().plot(kind = 'pie', figsize =(8,6))
plt.title("Male Female ratio")
plt.legend(['Male','Female']);

print(pd.crosstab(df.target, df.sex))
print()
sns.countplot(x = 'target', data = df, hue = 'sex')
plt.title("Heart Disease frequency for sex")
plt.xlabel("1 = Heart Disese, 0 = No Heart disease");

print(df.cp.value_counts())
print()
df.cp.value_counts().plot(kind = 'bar', color = ['salmon','lightskyblue','springgreen','khaki'])
plt.title("Chest pain type vs count")

print(pd.crosstab(df.sex,df.cp))
print()
pd.crosstab(df.sex,df.cp).plot(kind = 'bar', color = ['coral','lightskyblue','plum','khaki'])
plt.xlabel("1 = Male, 0 = Female");

print(pd.crosstab(df.cp,df.target))
print()

sns.countplot(x = 'cp', data = df, hue = 'target');

sns.displot(x='age', data =df, bins =30, kde = True);

sns.displot(x='thalach', data =df, bins =30, kde = True, color = 'chocolate');


