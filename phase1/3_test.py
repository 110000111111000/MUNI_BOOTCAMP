##Plot the hourly distribution of total complaints activity in a bar plot. \
##(Use the 'created_date' column to get the hour for each complaint record)

import pandas as pd
import matplotlib.pyplot as plt

## Get the data
file_path = "/Users/baharspring/" + \
"MUNI_Data_Analytics/nyc_311_data_2022.csv"
df = pd.read_csv(file_path)

## Check the data ,complaint type
#print(df['complaint_type'].tail(10))
#print(df.groupby(['complaint_type']).value_counts())
print('created_date type:',df.created_date.dtypes)
print('complaint_type: ',df.complaint_type.dtypes)

df['created_date'] = pd.to_datetime(df['created_date'])
#print(df['created_date'])

df['hour_column'] = df['created_date'].dt.hour
#print(df['hour_column'][1500])

unique_hour = df['hour_column'].nunique()
#print('unique_hour:',unique_hour)


sum_of_type_of_complaint_for_each_hour  = df.groupby(df['hour_column']).complaint_type.sum()
total_number_of_complaint_in_each_hour = df.groupby(df['hour_column']).complaint_type.count()

print('sum_of_type_of_complaint_for_each_hour:', sum_of_type_of_complaint_for_each_hour)
print('total_number_of_complaint_in_each_hour:', total_number_of_complaint_in_each_hour)




plt.bar(total_number_of_complaint_in_each_hour.index, total_number_of_complaint_in_each_hour, color='skyblue')

plt.xlabel('Hour')
plt.ylabel('Total complaint per Hours')
plt.title('Hourly distribution of total complaints activity')
plt.savefig('3.png')
plt.show()


