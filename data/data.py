import matplotlib.pyplot as plt # https://matplotlib.org/
import seaborn as sns # https://seaborn.pydata.org/
import pandas as pd # https://pandas.pydata.org/
# import numpy as np # https://numpy.org/

x = [1,2,3,4,5]
y = [4,8,2,3,1]

## matplotlib for basic data viz
plt.scatter(x, y)
# plt.bar(x, y)
# plt.line(x,y)
# plt.boxplot(x,y)
# plt.barbs(x,y)
plt.show()



## seaborn for fancier data viz
# data = [[1,4,5], [2,8,4], [3,2,7], [4,3,3], [5,1,5]]
# sns.heatmap(data)
# sns.violinplot(data)
# plt.show()



## pandas for handling dataframes
df = pd.read_csv("books.csv") # usecols=['num_pages', 'average_rating']
print(df.head(10)) # head() & tail() defaults to 5

## drop rows where pages are less than 30 or over 1000
df.drop(df[df.num_pages < 100].index, inplace=True)
df.drop(df[df.num_pages > 1000].index, inplace=True)

## plot with seabornn
sns.lmplot(x='num_pages', y='average_rating', data=df.sample(100))
plt.show()