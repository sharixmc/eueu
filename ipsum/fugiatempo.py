import pandas as pd

# Sample DataFrame
data = {
    'platform': ['android', 'ios', 'android', 'web'],
    'event_time': ['2020-01-15', '2020-02-20', '2020-03-10', '2020-01-25']
}
df = pd.DataFrame(data)

# Converting event_time to datetime
df['event_time'] = pd.to_datetime(df['event_time'])

# Filtering the DataFrame
filtered_df = df[(df['platform'] == 'android') &
                 (df['event_time'].between('2020-01-01', '2020-04-01'))]

print(filtered_df)
