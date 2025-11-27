import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Show Dataset
df = pd.read_csv('data_testing/dataset_shopify.csv')
df.head()

#Show Info dataset
df.info

#call event_timestamp
df['event_timestamp'] = pd.to_datetime(df['event_timestamp'])
df.info()

#change event_timestamp to datetime
df['date'] = df['event_timestamp'].dt.date
df.head()

#named channel to organic
df['channel'] = df['channel'].fillna('organic')
df.head()

#Showing top 10 countries by access frequency
country_counts = df['country'].value_counts()
top_10_countries = country_counts.head(10)
print("Top 10 Countries by Access Frequency:\n")
print(top_10_countries)

#display the bar from datasets (top 10 countries)
plt.figure(figsize=(10, 6))
plt.bar(top_10_countries.index, top_10_countries.values, color='skyblue')
plt.title('Top 10 Countries by Access Frequency')
plt.xlabel('Country')
plt.ylabel('Access Frequency')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

#checking mountly trends (cleansing data)
df['year'] = df['event_timestamp'].dt.year
df['month'] = df['event_timestamp'].dt.month
df.head()
#show MAU (monthly active users)
mau_per_channel = df.groupby(['year', 'month', 'channel'])['user_id'].nunique().reset_index()
mau_per_channel.columns = ['year', 'month', 'channel', 'mau']
mau_per_channel.head()

#Display the bar of MAU (Monthly Active Users)
mau_per_channel['year_month'] = mau_per_channel['year'].astype(str) + '-' + mau_per_channel['month'].astype(str).str.zfill(2)
plt.figure(figsize=(12, 7))
for channel in mau_per_channel['channel'].unique():
    channel_data = mau_per_channel[mau_per_channel['channel'] == channel]
    plt.plot(channel_data['year_month'], channel_data['mau'], label=channel, marker='o', markersize=4)
plt.title('Monthly Active Users (MAU) per Channel Over Time')
plt.xlabel('Year-Month')
plt.ylabel('Monthly Active Users (MAU)')
plt.xticks(rotation=45, ha='right')
plt.legend(title='Channel')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

