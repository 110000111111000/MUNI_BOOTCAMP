import pandas as pd
import numpy as np

# Get the data
file_path = "/Users/baharspring/" + \
"MUNI_Data_Analytics/nyc_311_data_2022.csv"
df = pd.read_csv(file_path)

# Quick check of the data
#print('First raws:', df.head(10))
#print('Last raws:', df.tail())
print('Types of features:', df.dtypes)
#print('General information:', df.info)

list_unique_key =[]
for i in range(len(df['unique_key'])):
#	print('i:',i,'unique_key:',df['unique_key'][i])
	list_unique_key.append(df['unique_key'][i])
#print('Number of raws:',len(list_unique_key))

duplicate_values = df['unique_key'].duplicated()

# Check if any duplicate values are found
if duplicate_values.any():
    print("There are duplicate values in the column.")
else:
    print("All values in the column unique_key are unique.")
# Creating a new cleaned copy

df_cleaned = df.dropna(subset=['incident_zip','longitude','latitude'])
#print('Number of raws with longitude, incident_zip, latitude valid values:',len(df_cleaned))
#print(len(df_cleaned))

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
seriesa = pd.Series(list_nan_longitude_unique_key)
seriesb = pd.Series(list_nan_latitude_unique_key)
seriesc = pd.Series(list_nan_incident_zip_unique_key)
seriesv =pd.Series(list_unique_key)
seriesv_seriesa = seriesv[~seriesv.isin(seriesa)]
seriesv_seriesa_seriesb = seriesv_seriesa[~seriesv_seriesa.isin(seriesb)]
seriesv_seriesa_seriesb_seriesc = seriesv_seriesa_seriesb[~seriesv_seriesa_seriesb.isin(seriesc)]

print('len seriesv - seriesa RED:',len(seriesv_seriesa))
print('len seriesva - seriesb Green:', len(seriesv_seriesa_seriesb))
print('len seriesvaa - seriesc Yellow:', len(seriesv_seriesa_seriesb_seriesc))

len_listv_lista = len(list_unique_key) - len(list_nan_incident_zip)
print(len_listv_lista)
len_listva_listb = len_listv_lista - len(list_nan_latitude)
#print('list green ', len_listva_listb)
list_listv_lista = [list_unique_key - list_nan_longitude for list_unique_key, list_nan_longitude in zip(list_unique_key, list_nan_longitude)]

#print('len subtraction of len list v - lista ', len_listv_lista)
#print('len list subtraction v and a', len(list_listv_lista))





common_elements_v_1 = pd.Index(seriesv).intersection(seriesa)
common_count_in_seriesv_seriesa = len(common_elements_v_1)
#print('len common element in v and 1',len(common_elements_v_1))

# Find the intersection of unique elements
common_elements = pd.Index(seriesa).intersection(seriesb).intersection(seriesc)

# Get the count of common unique elements
common_count_in_3_list = len(common_elements)

#print("Number of unique elements common in all three lists:", common_count_in_3_list)

#print(len(df_cleaned) + len(list_nan_longitude) + len(list_nan_latitude) + len(list_nan_incident_zip)) 

#nan_indices = df[df['longitude'].isna()].index
#print("Indices where 'longitude' values are NaN:", nan_indices)


data_for_December_2022 = df[df['created_date'].str.startswith('2022-12')]

#print('\nResult dataframe:\n', data_for_December_2022)
#print('Number of Data of December 2022:',len(data_for_December_2022))

#print(df['complaint_type'])

#print(df.groupby(['complaint_type]).sum())




