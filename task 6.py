import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Movies.csv')
print("First five rows of the dataset:")
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

print("questions = ")
print("1. Which genre has the highest average profitability?")
print("2. What is the trend of movie profits over the years?")
print("3. What is the distribution of movies by their opening weekend earnings?")
print("4. What is the relationship between budget and profitability?")
print("5. How do foreign gross earnings compare with domestic earnings across genres?")
print("6. What is the distribution of maximum heart rate for people with and without heart disease?")
print("7. How does the exercise induced angina relate to heart disease?")

avg_profitability = df.groupby('Genre')['Profitability'].mean().sort_values(ascending=False)
print("\nAverage Profitability by Genre:")
print(avg_profitability)

plt.figure(figsize=(10, 6))
avg_profitability.plot(kind='bar', color='skyblue')
plt.title('Average Profitability by Genre')
plt.xlabel('Genre')
plt.ylabel('Average Profitability')
plt.xticks(rotation=45)
plt.savefig('1.png') 
plt.clf() 

profit_by_year = df.groupby('Year')['Profitability'].sum()
print("\nProfitability by Year:")
print(profit_by_year)

plt.figure(figsize=(10, 6))
profit_by_year.plot(kind='line', marker='o', color='green')
plt.title('Movie Profitability Trend Over the Years')
plt.xlabel('Year')
plt.ylabel('Total Profitability')
plt.grid(True)
plt.savefig('2.png') 
plt.clf() 

print("\nOpening Weekend Earnings Summary:")
print(df['OpeningWeekend'].describe())

plt.figure(figsize=(10, 6))
sns.histplot(df['OpeningWeekend'], bins=30, kde=True, color='purple')
plt.title('Distribution of Opening Weekend Earnings')
plt.xlabel('Opening Weekend Earnings (in millions)')
plt.ylabel('Number of Movies')
plt.savefig('3.png') 
plt.clf() 

print("\nSummary of Budget and Profitability:")
print(df[['Budget', 'Profitability']].describe())

plt.figure(figsize=(10, 6))
sns.scatterplot(x=df['Budget'], y=df['Profitability'], color='orange')
plt.title('Budget vs Profitability')
plt.xlabel('Budget (in millions)')
plt.ylabel('Profitability')
plt.savefig('4.png') 
plt.clf() 

genre_gross = df.groupby('Genre')[['DomesticGross', 'ForeignGross']].sum()
print("\nDomestic and Foreign Gross by Genre:")
print(genre_gross)

genre_gross.plot(kind='bar', stacked=True, figsize=(10, 6), color=['blue', 'red'])
plt.title('Domestic vs Foreign Gross by Genre')
plt.xlabel('Genre')
plt.ylabel('Gross Earnings (in millions)')
plt.xticks(rotation=45)
plt.savefig('5.png') 
plt.clf() 


