import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv("tips.csv")
data.head(10)

plt.scatter(data['year'],data['own'])
plt.title('scatter plot')
plt.xlabel('year')
plt.ylabel('own')
plt.show()

plt.plot(data['year'])
plt.plot(data['own'])
plt.title('line chart')
plt.xlabel('year')
plt.ylabel('own')
plt.show()

plt.bar(data['year'], data['own'])
plt.title('bar plot')
plt.xlabel('year')
plt.ylabel('own')
plt.show()

plt.hist(data['income'])
plt.title('histogram')
plt.show()
