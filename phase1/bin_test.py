import pandas as pd
import matplotlib.pyplot as plt

## Get the data
file_path = "/Users/baharspring/" + \
"MUNI_Data_Analytics/nyc_311_data_2022.csv"
df = pd.read_csv(file_path)

## Print 5 raws of created_date column
#print(df['created_date'])

## Print 5 raws of datatime function 
df['date_time'] = pd.to_datetime(df['created_date'])
#print(df['date_time'])

df['hour'] = df['date_time'].dt.hour
print(df['hour'])


#df['minute'] = df['date_time'].dt.minute
#print(df['minute'].head(20))

#df['second'] = df['date_time'].dt.second
#print(df['second'].head(100))

bins = []
print('min float:',float(min(df['hour'])))
print('max float:',float(max(df['hour'])))
for i in range (min(df['hour']) , 25):
	print(i)
print(bins)




df['binned_hour'] =pd.cut(df['hour'].head(100), bins= 4) #,right = True , include_lowest= True)
print('df[binned_hour]',df['binned_hour'])


#df['binned_second'] =pd.cut(df['second'].head(100), bins= 4 ,right = True , include_lowest= True)
#print('df[binned_second]',df['binned_second'].head(100))

#print(df['binned_hour'].value_counts(sort = False))


