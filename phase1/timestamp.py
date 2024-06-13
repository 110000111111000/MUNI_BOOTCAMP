import pandas as pd 


  
# input current timestamp 
date = pd.Timestamp.now() 
print("currentTimestamp: ", date) 
  
# extract the Hours from the timestamp 
frame = date.hour 
print("Hour: ", frame) 


## Get the data
file_path = "/Users/baharspring/" + \
"MUNI_Data_Analytics/nyc_311_data_2022.csv"
df = pd.read_csv(file_path)

print('created_date type:',df.created_date.dtypes)
print('complaint_type: ',df.complaint_type.dtypes)

#date = pd.Timestamp(df['created_date']) 
#print (date)

data = pd.timedelta(df['created_date'])
print (date)

#print("Hour: ", date.hour)