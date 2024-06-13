import pandas as pd
import numpy as np

## Get the data
file_path = "/Users/baharspring/" + \
"MUNI_Data_Analytics/nyc_311_data_2022.csv"
df = pd.read_csv(file_path)

## Quick check of the data
#print('First raws:', df.head(10))
#print('Last raws:', df.tail())
#print('Types of features:', df.dtypes)
#print('General information:', df.info)

## check if we have dupicate raws
duplicate_values = df.duplicated(['unique_key'])
print('The number of rows in the DataFrame that have the same value in the unique_key column, \
 indicating duplicate rows:',duplicate_values.sum())

## 1.a_Remove the data records where either the 'incident_zip', 'latitude', or 'longitude' columns,have missing values or NaN
df_cleaned = df.dropna(subset=['incident_zip','longitude','latitude'])
print('Number of raws with longitude, incident_zip, latitude valid values:',len(df_cleaned))


## Test the cleaning data is correct
#a = pd.isna(df['incident_zip'])
#print(a.sum())
#b = pd.isna(df['longitude'])
#print(b.sum())
#c = pd.isna(df['latitude'])
#print(c.sum())

list_unique_key =[]
for i in range(len(df['unique_key'])):
#	print('i:',i,'unique_key:',df['unique_key'][i])
	list_unique_key.append(df['unique_key'][i])
#print('Number of raws:',len(list_unique_key))

list_nan_longitude = []
list_nan_longitude_unique_key = []
for i in range(len(df['longitude'])):
	if (pd.isna(df['longitude'][i])):
		#print('unique_key:',df['unique_key'][i])
		list_nan_longitude_unique_key.append(df['unique_key'][i])
		list_nan_longitude.append(df['longitude'][i])
#print('Number of raws with longitude colum is Nan:',len(list_nan_longitude)) 
#print('Number of unique_key in list_nan_longitude_unique_key', len(list_nan_longitude_unique_key))

list_nan_incident_zip =[]
list_nan_incident_zip_unique_key = []
for i in range(len(df['incident_zip'])):
	if pd.isna(df['incident_zip'][i]):
		list_nan_incident_zip_unique_key.append(df['unique_key'][i])
		list_nan_incident_zip.append(df['incident_zip'][i])
#print('Number of raws with incident_zip colum is Nan:',len(list_nan_incident_zip))
#print('Number of unique_key in list_nan_incident_zip_unique_key', len(list_nan_incident_zip_unique_key))

list_nan_latitude =	[]
list_nan_latitude_unique_key = []
for i in range(len(df['latitude'])):
	if pd.isna(df['latitude'][i]):
		list_nan_latitude_unique_key.append(df['unique_key'][i])
		list_nan_latitude.append(df['latitude'][i])
#print('Number of raws with latitude colum is Nan:',len(list_nan_latitude)) 
#print('Number of unique_key in list_nan_latitude_unique_key', len(list_nan_latitude_unique_key))

# Assuming list1, list2, and list3 are your three lists of unique keys
# Convert lists to pandas Series
u = pd.Series(list_unique_key)
a = pd.Series(list_nan_longitude_unique_key)
b = pd.Series(list_nan_latitude_unique_key)
c = pd.Series(list_nan_incident_zip_unique_key)



seta = set(a)
#print(len(seta))

setb = set(b)
#print(len(setb))

setc = set(c)
#print(len(setc))

aUbUc = seta.union(setb).union(setc)
#print("seta U setb U setc :",len(aUbUc))

#print(len(u))
subset_u = u[~u.isin(aUbUc)]
#print(len(subset_u))
if (len(df_cleaned) == len(subset_u)):
	print('Congradulation, The data has been reduced correct.')

##1.b_Filter the 'created_date' column to keep the data just for December 2022.
## Check the  5 raws of created_data 
#print(df_cleaned['created_date'].head(5))
#print(df_cleaned['created_date'].tail(5))

pattern = '2022-12'
data_cleaned_for_December_2022_filtered = df_cleaned[df_cleaned['created_date'].str.startswith(pattern)]
print('Number of raws  of the data just for December 2022:', len(data_cleaned_for_December_2022_filtered))

data_cleaned_for_December_2022 = df_cleaned['created_date'].str.contains(pattern)

#print(data_cleaned_for_December_2022.head(5))
#print(data_cleaned_for_December_2022.sum())
if (len(data_cleaned_for_December_2022_filtered) == data_cleaned_for_December_2022.sum()):
	print('Congradulation, The data has been filtered correct.')

















