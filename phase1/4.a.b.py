
##4a.Evaluate the service processing times for city agencies
##Get the processing time for each data record. 
##Columns 'created_date' represents the time when the complaint was made and 'closed_date' when it was resolved. 


##4b.Get the median processing time by each city agency and sort to get 
##the three fastest and three slowest city agencies (the 'agency_name' column represents the city agency)


from datetime import datetime, timedelta
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


## Get the data
file_path = "/Users/baharspring/" + \
"MUNI_Data_Analytics/nyc_311_data_2022.csv"
df = pd.read_csv(file_path)

#print(df.columns)
#print(df[df.columns[0:4]].head(10))

##select the numbers of raws 1:3
#print(df.loc[8:10], ['unique_key','created_date','closed_date'])

#print(df[['unique_key','created_date','closed_date']])
## Print raws of created_date and closed_date column

## cleaned the raws with nan value at created_date and closed_date columns 
df_cleaned = df.dropna(subset=['created_date','closed_date'])
#print('Number of raws with valid values:',len(df_cleaned))

## calculate time duration
df_time_processing = pd.to_datetime(df_cleaned.closed_date) - pd.to_datetime(df_cleaned.created_date)

#Convert  negative time duration to positive by abs
#df_time_processing = abs(pd.to_datetime(df_cleaned.closed_date) - pd.to_datetime(df_cleaned.created_date)


negative_durations_time = df_time_processing[df_time_processing < pd.Timedelta(0)]
#print(negative_durations_time)

# Print the DataFrame with only positive time processing durations
positive_durations_time = df_time_processing[df_time_processing >= pd.Timedelta(0)]
#print(positive_durations_time)

## Print descriptions
#print(df_time_processing.describe())
#print(negative_durations_time.describe())
#print(positive_durations_time.describe())

positive_durations_time_data = df_cleaned[df_time_processing > pd.Timedelta(0)]
#print(positive_durations_time_data.loc[4:6])
positive_durations_time_data['processing_time'] = df_time_processing[df_time_processing >= pd.Timedelta(0)]
#print(positive_durations_time_data.processing_time[0]) 

#print(positive_durations_time_data.describe())

complaint_by_agency = positive_durations_time_data.groupby(df['agency_name']).processing_time.median()
#print(complaint_by_agency.head(50))

fastest_three_agencies = complaint_by_agency.nlargest(3).index
slowest_three_agencies = complaint_by_agency.nsmallest(3).index
print("Fastest:",slowest_three_agencies)
print("Slowest:",fastest_three_agencies)



