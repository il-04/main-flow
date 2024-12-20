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

print(df.describe())
print()

print(df.info())
print()

print("questions = ")
print("1. What is the trend of movie profits over the years?")
print("2. What is the distribution of movies by their opening weekend earnings?")
print("3. How do foreign gross earnings compare with domestic earnings across genres?")
print("4. Which Leadstudio has the highest average profitability?")
print("5. What is the relationship between profitability and audience score?")
print("6. What is the total world gross by genre?")
print("7. What is the distribution of movie genres in the dataset?")

profit_by_year = df.groupby('Year')['Profitability'].sum()
print(profit_by_year)
plt.figure(figsize=(10, 6))
profit_by_year.plot(kind='line', marker='o', color='green')
plt.title('Movie Profitability Trend Over the Years')
plt.xlabel('Year')
plt.ylabel('Total Profitability')
plt.grid(True)
plt.savefig('1.png') 
plt.clf() 

print(df['OpeningWeekend'].describe())
plt.figure(figsize=(10, 6))
sns.histplot(df['OpeningWeekend'], bins=30, kde=True, color='purple')
plt.title('Distribution of Opening Weekend Earnings')
plt.xlabel('Opening Weekend Earnings (in millions)')
plt.ylabel('Number of Movies')
plt.savefig('2.png') 
plt.clf() 

genre_gross = df.groupby('Genre')[['DomesticGross', 'ForeignGross']].sum()
print(genre_gross)
genre_gross.plot(kind='bar', stacked=True, figsize=(10, 6), color=['blue', 'red'])
plt.title('Domestic vs Foreign Gross by Genre')
plt.xlabel('Genre')
plt.ylabel('Gross Earnings (in millions)')
plt.xticks(rotation=45)
plt.savefig('3.png') 
plt.clf() 

studio_profitability = df.groupby('LeadStudio')['Profitability'].mean().sort_values(ascending=False)
print(studio_profitability)
plt.figure(figsize=(10, 6))
studio_profitability.plot(kind='bar', color='lightcoral')
plt.title('Average Profitability by Studio')
plt.xlabel('Lead Studio')
plt.ylabel('Average Profitability')
plt.xticks(rotation=45)
plt.savefig('4.png')
plt.clf()

print(df[['Profitability', 'AudienceScore']].describe())
plt.figure(figsize=(10, 6))
sns.scatterplot(x=df['AudienceScore'], y=df['Profitability'], color='brown')
plt.title('Profitability vs Audience Score')
plt.xlabel('Audience Score')
plt.ylabel('Profitability')
plt.savefig('5.png')
plt.clf()

plt.figure(figsize=(10, 6))
world_gross_by_genre = df.groupby('Genre')[['DomesticGross', 'ForeignGross']].sum().sum(axis=1)
world_gross_by_genre.plot(kind='bar', color='limegreen')
plt.title('Total World Gross by Genre')
plt.xlabel('Genre')
plt.ylabel('World Gross (in millions)')
plt.xticks(rotation=45)
plt.savefig('6.png')
plt.clf()

print(df['Genre'].value_counts())
genre_counts = df['Genre'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(genre_counts, labels=genre_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("Set3", len(genre_counts)))
plt.title("Distribution of Movie Genres")
plt.axis('equal')  
plt.savefig('7.png') 
plt.clf() 
