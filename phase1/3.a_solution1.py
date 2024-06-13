import pandas as pd
import matplotlib.pyplot as plt

## Get the data
file_path = "/Users/baharspring/" + \
"MUNI_Data_Analytics/nyc_311_data_2022.csv"
df = pd.read_csv(file_path)

## Print raws of created_date column
#print(df['created_date'])

## Print raws of datatime function 
df['date_time'] = pd.to_datetime(df['created_date'])
#print(df['date_time'])

df['hour'] = df['date_time'].dt.hour
#print(df['hour'])

bins = []
for i in range (min(df['hour']), (max(df['hour']) + 2) ):
	bins.append(i)
#print(bins)

df['binned_hour'] = pd.cut(df['hour'], bins= bins ,right = False , include_lowest= False)
#print('df[binned_hour]',df['binned_hour'])
#print(df['binned_hour'].value_counts(sort = False))

#top_3_complaint= df.complaint_type.value_counts(normalize = False).nlargest(3)
#print('top_3_complaint in 24 hours:', top_3_complaint)

def plot_top_three_complaints(df):
    
    # Filter the DataFrame for the top three complaint types
    top_three_complaints = df['complaint_type'].value_counts().nlargest(3).index
    #print(top_three_complaints)

    top_three_df = df[df['complaint_type'].isin(top_three_complaints)]
    #print(top_three_df.complaint_type.head(50))

    top_three_df_hour_binned = top_three_df['binned_hour'].value_counts(sort = False)
    #print(top_three_df_hour_binned)

    # Group the filtered DataFrame by 'created_date' hour and 'complaint_type', and count occurrences
    hourly_complaint_counts = top_three_df.groupby([top_three_df['binned_hour'], 'complaint_type'],observed=False).size().unstack(fill_value=0)
    #print(hourly_complaint_counts)

    # Calculate the total count of the top three complaint types for each hour
    total_counts_top_three = hourly_complaint_counts.sum(axis=1)
    #print(total_counts_top_three)

    # Calculate the percentage of each of the top three complaint types for each hour
    percentage_top_three = (hourly_complaint_counts.div(total_counts_top_three, axis=0) * 100)
    #print(percentage_top_three)
    
    percentage_top_three.plot(title = 'Relative Proportions of Top Three Complaint Types by Hour',
        xlabel= 'Relative Proporition of Complaint Types (%)',
        label='test',
        ylabel = 'Hour',
        kind = 'barh',
        stacked = False,# False
        mark_right = True)
    plt.savefig('3.aa1.png')
    plt.show()
    

plot_top_three_complaints(df)