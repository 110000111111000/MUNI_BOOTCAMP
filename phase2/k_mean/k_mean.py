import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np 
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
from sklearn import metrics
from scipy.spatial.distance import cdist


## Get the data
df = pd.read_csv('Mall_Customers.csv')
## Select 4 features for clustering

## Select two features for clustering
X = df[['Annual Income (k$)', 'Spending Score (1-100)']]

df["Age"]= df["Age"].astype(np.int64)
df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1})
df['Gender']= df["Gender"].astype(np.int64)



## Normalize the data
scaler = MinMaxScaler()
#scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
#print('X two Features after normalize:', X_scaled)

df_X_scaled = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)
#print(df_X_scaled.columns)

data = X_scaled
inertias = []

for i in range(1,20):
    kmeans = KMeans(n_clusters=i)
    kmeans.fit(data)
    inertias.append(kmeans.inertia_)

plt.plot(range(1,20), inertias, marker='o')
plt.title('Elbow method')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.show()

kmeans = KMeans(n_clusters=5)
kmeans.fit(data)

plt.scatter(X_scaled[:,0],X_scaled[:,1], c=kmeans.labels_)
plt.show()