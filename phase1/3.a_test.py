#Plot the relative proportions (%) for each hour of the top three complaint types, where the
#percentages are calculated based on the total count of these three types only. Each of the
#three complaint types can be visualized by a separate color. (Use the &#39;created_date&#39;
#column to get the hour for each complaint record).

import pandas as pd
import matplotlib.pyplot as plt

## Get the data
file_path = "/Users/baharspring/" + \
"MUNI_Data_Analytics/nyc_311_data_2022.csv"
df = pd.read_csv(file_path)

df['created_date'] = pd.to_datetime(df['created_date'])
#print(df['created_date'])

df['hour_column'] = df['created_date'].dt.hour
print(df['hour_column'])

print('min: hour', min(df['hour_column']), 'max:hour,',max(df['hour_column']))
bins = []
for i in range (min(df['hour_column'])-2, max(df['hour_column'])+2,1):
	bins.append(i)
print(bins)

df['hour_column_binned'] = pd.cut(df['hour_column'], bins, precision=3)
print(df['hour_column_binned'])
#print(df)

gh = df['hour_column_binned'].value_counts()
print('gh:',gh)

#counts = pd.cut(s, 3, labels=['S', 'M', 'L']).value_counts()


sum_of_type_of_complaint_for_each_hour  = df.groupby(df['hour_column_binned'], observed=False).complaint_type.sum()
print('show_of_type_of_complaint_for_each_hour',sum_of_type_of_complaint_for_each_hour)

total_number_of_complaint_in_each_hour = df.groupby(df['hour_column_binned'],observed=False).complaint_type.count()
print('total_number_of_complaint_in_each_hour:', total_number_of_complaint_in_each_hour)

#top_tree_number_of_complaint_in_each_hour = df.groupby(df['hour_column_binned'],observed=True).complaint_type.value_counts(normalize = False).nlargest(3)
#print('top_tree_number_of_complaint_in_each_hour:' , top_tree_number_of_complaint_in_each_hour)

#a = df.complaint_type.value_counts(normalize = True).nlargest(5)



