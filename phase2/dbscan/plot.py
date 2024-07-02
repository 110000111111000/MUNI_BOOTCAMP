import pandas as pd 
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
import numpy as np 

##Get the data
#file_path = "/Users/baharspring/MUNI_Data_Analytics/phase2/Mall_Customers.csv"
df = pd.read_csv('Mall_Customers.csv')

df["Age"]= df["Age"].astype(np.int64)
df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1})
df['Gender']= df["Gender"].astype(np.int64)


attributes = ["Age", "Gender", "Annual Income (k$)",
              "Spending Score (1-100)", "CustomerID" ]
custom_color = (0.6, 0.1, 0.8)              

scatter_options = {'color': 'purple'}              
hist_options = {'color': custom_color}

axes = scatter_matrix(df[attributes], figsize=(18, 16),hist_kwds=hist_options,color='purple' )

# Adjust the font size for the tick labels and axis labels
# Adjust the font size for the tick labels and axis labels
for ax in axes.ravel():
    ax.xaxis.label.set_fontsize(6)
    ax.yaxis.label.set_fontsize(6)
    ax.xaxis.label.set_fontweight('bold')
    ax.yaxis.label.set_fontweight('bold')
    ax.tick_params(axis='both', which='major', labelsize=6)

# Set a stylish color for the background
plt.gcf().set_facecolor('lightgrey')

plt.savefig('scatter_matrix_plot.png',dpi=600)  # extra code
plt.show()
