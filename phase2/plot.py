import pandas as pd 
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
import numpy as np 

##Get the data
#file_path = "/Users/baharspring/MUNI_Data_Analytics/phase2/Mall_Customers.csv"
df = pd.read_csv('Mall_Customers.csv')

df["Age"].astype(np.int64)
attributes = ["Age", "Gender", "Annual Income (k$)",
              "Spending Score (1-100)", "CustomerID" ]
scatter_matrix(df[attributes], figsize=(12, 8),color ='b')
#save_fig("scatter_matrix_plot")  # extra code
plt.show()
