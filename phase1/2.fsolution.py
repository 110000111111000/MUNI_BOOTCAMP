import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

## Get the data
file_path = "/Users/baharspring/" + \
"MUNI_Data_Analytics/nyc_311_data_2022.csv"
df = pd.read_csv(file_path)
df_cleaned = df.dropna(subset=['incident_zip','longitude','latitude'])
pattern = '2022-12'
data_cleaned_for_December_2022_filtered = df_cleaned[df_cleaned['created_date'].str.startswith(pattern)]
print('Number of raws  of the data just for December 2022:', len(data_cleaned_for_December_2022_filtered))

## Check the data ,complaint type
#print(df['complaint_type'].tail(10))
#print(df.groupby(['complaint_type']).sum())

## Check the total number of complaint
num_unique_complaints = data_cleaned_for_December_2022_filtered['complaint_type'].nunique( dropna = True)
#print("Number of different types of complaints:", num_unique_complaints)

## 	Count the total number non nan complaint type
non_nan_count_complaint_type = data_cleaned_for_December_2022_filtered['complaint_type'].count()
#print("Number of non_nan_count_complaint_type:", non_nan_count_complaint_type)

# Get the total number of requests for each complaint type
total_requests_per_complaint = data_cleaned_for_December_2022_filtered['complaint_type'].value_counts()
#By default, value_counts will sort the data by numeric count in descending order.
# Display the result
print("Total number of occurrance for each complaint type:")
print(total_requests_per_complaint)

#the percent of total records, using the normalize parameter
a = data_cleaned_for_December_2022_filtered.complaint_type.value_counts(normalize = True).nlargest(5)
print('sum_top_5:' ,sum(a))
b = 1 - sum(a)
print('other complain:', b)

percentages = list(a.values) + [b]
print(percentages)

## Generate pastel colors with adjusted lightness
num_colors = 6
pastel_colors = plt.cm.get_cmap('Pastel1', num_colors)

# Adjust the lightness of the colors
lightness_factor = 1  # Adjust as needed (0 to 1)
adjusted_pastel_colors = pastel_colors(np.linspace(0, 1, num_colors)) * lightness_factor

# Convert adjusted colors to list
adjusted_pastel_colors_list = [tuple(color) for color in adjusted_pastel_colors]

# Display the list of adjusted pastel colors
print("Adjusted pastel colors:")
print(adjusted_pastel_colors_list)

# Plot a pie chart using adjusted pastel colors
sizes = np.random.rand(num_colors)



#mycolors = ["c", "pink", "m", "#4CAF50", "yellow" , "blue"]
mylabels = ["HEAT/HOT WATER", "Illegal Parking", "Noise - Residential", "Blocked Driveway", "UNSANITARY CONDITION", "Other Complaint"]
plt.pie(percentages, labels = mylabels, colors = adjusted_pastel_colors_list, autopct='%1.1f%%')
plt.title('Top Five Complaint Types vs rest % Share')
plt.savefig('pieplot2.png')
plt.show()