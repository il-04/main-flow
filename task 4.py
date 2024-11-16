import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('USvideos.csv', delimiter='\t')
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

columns_to_remove = ['thumbnail_link','description']
df = df.drop(columns=columns_to_remove)
print(df.info())
print()

from datetime import datetime
import datetime
df["trending_date"] = df["trending_date"].apply(lambda x : datetime.datetime.strptime(x,'%y.%d.%m'))
print(df.head(3))
print()

df['publish_time'] = pd.to_datetime(df['publish_time'])
print(df.head(2))
print()

df['publish_month'] = df['publish_time'].dt.month
df['publish_day'] = df['publish_time'].dt.day
df['publish_hour'] = df['publish_time'].dt.hour
print(df.head(2))
print()

print(sorted(df["category_id"].unique()))
print()

df['category_name'] = np.nan
df['category_name'] = df['category_name'].astype('object')
df.loc[df["category_id"] == 1, "category_name"] = 'Film and Animation'
df.loc[df["category_id"] == 2, "category_name"] = 'Autos and Vehicles'
df.loc[df["category_id"] == 10, "category_name"] = 'Music'
df.loc[df["category_id"] == 15, "category_name"] = 'Pets and Animals'
df.loc[df["category_id"] == 17, "category_name"] = 'Sports'
df.loc[df["category_id"] == 19, "category_name"] = 'Travels and Events'
df.loc[df["category_id"] == 20, "category_name"] = 'Gaming'
df.loc[df["category_id"] == 22, "category_name"] = 'People and Blogs'
df.loc[df["category_id"] == 23, "category_name"] = 'Comedy'
df.loc[df["category_id"] == 24, "category_name"] = 'Entertainment'
df.loc[df["category_id"] == 25, "category_name"] = 'News and Politics'
df.loc[df["category_id"] == 26, "category_name"] = 'How to and Style'
df.loc[df["category_id"] == 27, "category_name"] = 'Education'
df.loc[df["category_id"] == 28, "category_name"] = 'Science and Technology'
df.loc[df["category_id"] == 29, "category_name"] = 'Non Profits and Activism'
df.loc[df["category_id"] == 30, "category_name"] = 'Movies'
df.loc[df["category_id"] == 43, "category_name"] = 'Shows'

df['publish_time'] = pd.to_datetime(df['publish_time'])
df['year'] = df['publish_time'].dt.year
yearly_counts = df.groupby('year')['video_id'].count()
yearly_counts.plot(kind='bar', xlabel='Year', ylabel='Total Publish Count', title='Total Published Videos per Year')
plt.savefig('yearly_publish_count.png')  # Saves the plot as a PNG file
plt.close()

df['publish_time'] = pd.to_datetime(df['publish_time'])
df['year'] = df['publish_time'].dt.year
yearly_views = df.groupby('year')['views'].sum()
yearly_views.plot(kind='bar', xlabel='Year', ylabel='Total Views', title='Total Views per Year')
plt.xticks(rotation=0)  
plt.tight_layout() 
plt.savefig('yearly_views.png')  
plt.close()

category_views = df.groupby('category_name')['views'].sum().reset_index()
top_categories = category_views.sort_values(by='views', ascending=False).head(5)
plt.bar(top_categories['category_name'], top_categories['views'])
plt.xlabel('Category Name', fontsize=12)
plt.ylabel('Total Views', fontsize=12)
plt.title('Top 5 Categories by Total Views', fontsize=15)
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.savefig('top_5_categories.png')
plt.close()

category_counts = df['category_name'].value_counts().index
plt.figure(figsize=(12,6))
sns.countplot(x='category_name', data=df, order=category_counts)
plt.xticks(rotation=90)
plt.title('Video Count by Category')
plt.savefig('video_count_by_category.png')
plt.close()

df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['publish_hour'] = df['publish_time'].dt.hour
videos_per_hour = df['publish_hour'].value_counts().sort_index()
plt.figure(figsize=(12, 6))
sns.barplot(x=videos_per_hour.index, y=videos_per_hour.values, palette='rocket')
plt.title('Number of Videos Published per Hour')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Videos')
plt.xticks(rotation=45)
plt.savefig('videos_per_hour_plot.png')
plt.close()

df['publish_time'] = pd.to_datetime(df['publish_time'])
df['publish_date'] = df['publish_time'].dt.date
video_count_by_date = df.groupby('publish_date').size()
plt.figure(figsize=(12,6))
sns.lineplot(data=video_count_by_date)
plt.title('Videos Published Over Time')
plt.xlabel('Publish Date')
plt.ylabel('Number of Videos',)
plt.xticks(rotation=45)
plt.savefig('video_count_by_date.png')
plt.close()

sns.scatterplot(data=df, x='views', y='likes')
plt.title('Views vs Likes')
plt.xlabel('Views')
plt.ylabel('Likes')
plt.savefig('views_vs_likes.png')
plt.close()

plt.figure(figsize = (14,8))
plt.subplots_adjust(wspace = 0.2, hspace = 0.4, top = 0.9)
plt.subplot(2,2,1)
g = sns.countplot(x= 'comments_disabled', data=df)
g.set_title("Comments Disabled", fontsize=16)
plt.subplot(2,2,2)
g1 = sns.countplot(x= 'ratings_disabled', data=df)
g1.set_title("Ratings Disabled", fontsize=16)
plt.subplot(2,2,3)
g2 = sns.countplot(x= 'video_error_or_removed', data=df)
g2.set_title("Video Error or Removed", fontsize=16)
plt.savefig('video_comments_ratings.png')
plt.close()

corr_matrix = df[['views', 'likes']].corr()
print(corr_matrix)
print()
