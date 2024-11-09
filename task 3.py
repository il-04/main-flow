import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv("tips.csv")
data.head(10)

plt.scatter(data['day'],data['tips'])
plt.title('scatter plot')
plt.xlabel('data')
plt.ylabel('tips')
plt.show()

plt.plot(data['day'])
plt.plot(data['tips'])
plt.title('line chart')
plt.xlabel('day')
plt.ylabel('tips')
plt.show()

plt.bar(data['day'], data['tips'])
plt.title('bar plot')
plt.xlabel('day')
plt.ylabel('tips')
plt.show()

plt.hist(data['tips'])
plt.title('histogram')
plt.show()
