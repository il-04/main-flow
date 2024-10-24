import pandas as pd
data = pd.read_csv("01.Data Cleaning and Preprocessing.csv")
type(data)
print()

a=data.info()
print()

print('concise summary\n',a)
b=data.describe()
print('descriptive statistics\n',b)
print()

c = data.drop_duplicates()
print('removed duplicate rows\n',c)
print()

d=data.isnull()
print('check null values\n',d)
print()

e=data.isnull().sum()
print('number of null values\n',e)
print()

f=data.isnull().sum().sum()
print('total null value\n',f)
print()

g=data.notnull()
print('check not null values\n',g)
print()

data2 = data.fillna(value=0)
print('replace null value to zero\n',data2)
print()

data3=data.fillna(method='pad')
print('filling null values by forward filling\n',data3)
print()

data4=data.fillna(method='bfill')
print('filling null values by backward filling\n',data4)
print()

import numpy as np
from scipy import stats
h=data2.columns
print('detect outliers\n',h)
print()

data2.drop(['Observation'], axis =1, inplace=True)
i=data2.columns
print('removed column\n',i)
print()

Q1 = data2.quantile(0.25)
Q3 = data2.quantile(0.75)
IQR=Q3-Q1
print(' interquartile range\n',IQR)
print()

data2=data2[~((data2<(Q1-1.5*IQR))|(data2>(Q3+1.5*IQR))).any(axis=1)]
print('clean dataset\n',data2)
print()

j=data2.describe()
print('descriptive statistics of the clean dataset\n',j)
