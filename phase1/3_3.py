##Plot the hourly distribution of total complaints activity in a bar plot. \
##(Use the 'created_date' column to get the hour for each complaint record)

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

## Get the data
file_path = "/Users/baharspring/" + \
"MUNI_Data_Analytics/nyc_311_data_2022.csv"
df = pd.read_csv(file_path)

## Check the data ,complaint type
#print(df['complaint_type'].tail(10))
#print(df.groupby(['complaint_type']).sum())
print('created_date type:',df.created_date.dtypes)
print('complaint_type: ',df.complaint_type.dtypes)


## Check the data ,created_date
print(df['created_date'].head(10))

df['created_date'] = pd.to_datetime(df['created_date'])
print(df['created_date'])

df['hour_column'] = df['created_date'].dt.hour
print(df['hour_column'])

complaints_by_hour = df.groupby('hour_column').size()
print(complaints_by_hour)
complaints_by_hour = complaints_by_hour.reindex(range(24), fill_value=0)
print(complaints_by_hour)

hour_data = df['hour_column'].value_counts().sort_index()

plt.bar(hour_data.index, hour_data.values)
plt.xlabel('Hour')
plt.ylabel('Frequency')
plt.title('Distribution of Hours')
plt.show()





## Split Method
#df[['date', 'time']] = df['created_date'].str.split( 'T' ,expand=True)
#print(df['date'])
#time_split = df['time'].str.split(':', expand=True)
#df['hour'] = time_split[0]
#df['min'] = time_split[1]
#df['sec'] = time_split[2]



