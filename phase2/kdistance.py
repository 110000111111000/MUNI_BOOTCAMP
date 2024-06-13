import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import NearestNeighbors

## Get the data
dfwithna = pd.read_csv('Mall_Customers.csv')
#print('Number of raws before dropping nan value',len(dfwithna))

## print all features
#print('Features:',dfwithna.columns)

## Drop rows with any missing values
df = dfwithna.dropna()
#print('Number of raws after dropping nan value',len(df))

df["Age"]= df["Age"].astype(np.int64)
df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1})

## Select two features for clustering
X = df[['Annual Income (k$)', 'Spending Score (1-100)','Gender', 'Age']]
#print('Max Annual Income',max(X.iloc[:,0]),'Min Annual Income:',min(X.iloc[:,0]))
#print('Max Spending Score',max(X.iloc[:,1]),'Min Spending Score:',min(X.iloc[:,1]))

# normalize the data
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)
#print('X two Features after normalize:', X_scaled)

k = 7
neighbors = NearestNeighbors(n_neighbors=k)
neighbors_fit = neighbors.fit(X_scaled)
distances, indices = neighbors_fit.kneighbors(X_scaled)

distances = np.sort(distances, axis=0)
distances = distances[:,1]
plt.plot(distances)
plt.show()






