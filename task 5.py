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
plt.savefig('1.png')  
plt.clf() 

print(df.describe())
print()

print("questions = ")
print("1. How many people have heart disease and how many people doesn't have heart disease")
print("2. People of which sex has most heart disease?")
print("3. People of which sex has which type of chest pain most?")
print("4. People with which chest pain are most prone to have heart disease?")
print("5. What is the distribution of age for people with heart disease vs people without heart disease?")
print("6. What is the relationship between blood pressure and heart disease?")
print("7. What is the average cholesterol level for people with and without heart disease?")
print("8. What is the distribution of maximum heart rate for people with and without heart disease?")
print("9. How does the exercise induced angina relate to heart disease?")
print("10. Is there any correlation between oldpeak and heart disease?")

print(df.target.value_counts())
print()
df.target.value_counts().plot(kind = 'bar',color = ["orchid","salmon"])
plt.title("Heart disease values")
plt.xlabel("1 = Heart Disese, 0 = No Heart disease")
plt.ylabel("Amount");
plt.savefig('2.png') 
plt.clf() 

df.target.value_counts().plot(kind = 'pie', figsize = (8,6))
plt.legend(["Disease","No Disease"]);
plt.savefig('3.png')  
plt.clf() 

print(df.sex.value_counts())
print()
df.sex.value_counts().plot().plot(kind = 'pie', figsize =(8,6))
plt.title("Male Female ratio")
plt.legend(['Male','Female']);
plt.savefig('4.png')  
plt.clf() 

print(pd.crosstab(df.target, df.sex))
print()
sns.countplot(x = 'target', data = df, hue = 'sex')
plt.title("Heart Disease frequency for sex")
plt.xlabel("1 = Heart Disese, 0 = No Heart disease");
plt.savefig('5.png')  
plt.clf() 

print(df.cp.value_counts())
print()
df.cp.value_counts().plot(kind = 'bar', color = ['salmon','lightskyblue','springgreen','khaki'])
plt.title("Chest pain type vs count")
plt.savefig('6.png')  
plt.clf() 

print(pd.crosstab(df.sex,df.cp))
print()
pd.crosstab(df.sex,df.cp).plot(kind = 'bar', color = ['coral','lightskyblue','plum','khaki'])
plt.xlabel("1 = Male, 0 = Female");
plt.savefig('7.png')  
plt.clf() 

print(pd.crosstab(df.cp,df.target))
print()

sns.countplot(x = 'cp', data = df, hue = 'target');
plt.savefig('8.png')  
plt.clf() 

sns.displot(x='age', data =df, bins =30, kde = True);
plt.savefig('9.png')  
plt.clf() 

sns.displot(x='thalach', data =df, bins =30, kde = True, color = 'chocolate');
plt.savefig('10.png')  
plt.clf() 

sns.displot(data=df, x='age', hue='target', kde=True, bins=30, aspect=1.5)
plt.title('Age Distribution for Heart Disease vs No Heart Disease')
plt.xlabel('Age')
plt.ylabel('Density')
plt.legend(title='Heart Disease', labels=['No Disease (0)', 'Disease (1)'])
plt.savefig('11.png')
plt.clf()

sns.boxplot(x='target', y='trestbps', data=df, hue='target', palette='coolwarm', legend=False)
plt.title('Blood Pressure vs Heart Disease')
plt.xlabel('Heart Disease (1 = Yes, 0 = No)')
plt.ylabel('Resting Blood Pressure (trestbps)')
plt.savefig('12.png')
plt.clf()

sns.boxplot(x='target', y='chol', data=df, hue='target', palette='coolwarm', legend=False)
plt.title('Cholesterol Levels vs Heart Disease')
plt.xlabel('Heart Disease (1 = Yes, 0 = No)')
plt.ylabel('Serum Cholesterol (chol)')
plt.savefig('13.png')
plt.clf()

sns.displot(data=df, x='thalach', hue='target', kde=True, bins=30, aspect=1.5, color='green')
plt.title('Maximum Heart Rate for Heart Disease vs No Heart Disease')
plt.xlabel('Maximum Heart Rate (thalach)')
plt.ylabel('Density')
plt.legend(title='Heart Disease', labels=['No Disease (0)', 'Disease (1)'])
plt.savefig('14.png')
plt.clf()

sns.countplot(x='exang', hue='target', data=df, palette='coolwarm')
plt.title('Exercise Induced Angina vs Heart Disease')
plt.xlabel('Exercise Induced Angina (1 = Yes, 0 = No)')
plt.ylabel('Count')
plt.legend(title='Heart Disease', labels=['No Disease (0)', 'Disease (1)'])
plt.savefig('15.png')
plt.clf()

sns.boxplot(x='target', y='oldpeak', data=df, hue='target', palette='coolwarm', legend=False)
plt.title('Oldpeak vs Heart Disease')
plt.xlabel('Heart Disease (1 = Yes, 0 = No)')
plt.ylabel('Depression Induced by Exercise (oldpeak)')
plt.savefig('16.png')
plt.clf()

