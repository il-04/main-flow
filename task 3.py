import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv('Book2.csv')  # This will skip problematic lines
print(data.head())

plt.scatter(data['day'],data['tip'])
plt.title('scatter plot')
plt.xlabel('data')
plt.ylabel('tip')
plt.show()

plt.plot(data['day'])
plt.plot(data['tip'])
plt.title('line chart')
plt.xlabel('day')
plt.ylabel('tip')
plt.show()

plt.bar(data['day'], data['tip'])
plt.title('bar plot')
plt.xlabel('day')
plt.ylabel('tip')
plt.show()

plt.hist(data['tip'])
plt.title('histogram')
plt.show()
