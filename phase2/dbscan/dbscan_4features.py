import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
import itertools
from mpl_toolkits.mplot3d import Axes3D
from pandas.plotting import scatter_matrix

from sklearn import metrics
from sklearn.cluster import DBSCAN
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import MinMaxScaler
#from sklearn.preprocessing import StandardScaler
from matplotlib.colors import ListedColormap, BoundaryNorm

from sklearn.model_selection import GridSearchCV
from sklearn.metrics import adjusted_rand_score
from sklearn.model_selection import ParameterGrid

## Get the data
dfwithna = pd.read_csv('Mall_Customers.csv')
#print('Number of raws before dropping nan value',len(dfwithna))

## Drop rows with any missing values
df = dfwithna.dropna()
#print('Number of raws after dropping nan value',len(df))

df["Age"]= df["Age"].astype(np.int64)

df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1})
df['Gender']= df["Gender"].astype(np.int64)

## Select two features for clustering
X = df[['Annual Income (k$)', 'Spending Score (1-100)', 'Gender', 'Age']]

## Normalize the data
scaler = MinMaxScaler()
#scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
#print('X four Features after normalize:', X_scaled)
#print(X_scaled.ndim)
print(X_scaled.shape)
df_X_scaled = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)
print(df_X_scaled.columns)


## plot k_distance graph to have an idea of epsilon range
k = 5
neighbors = NearestNeighbors(n_neighbors=k)
neighbors_fit = neighbors.fit(X_scaled)
distances, indices = neighbors_fit.kneighbors(X_scaled)

distances = np.sort(distances, axis=0)
distances = distances[:,1]
plt.plot(distances)
#plt.show()


## Grid search
epsilons = np.linspace(0.01,0.3, num = 1000)
#print(epsilons)
min_samples = np.arange(2,20, step = 2)
#print(min_samples)

combinations = list(itertools.product(epsilons, min_samples))
#print(combinations) 
N = len(combinations)
#print(N)



db = DBSCAN().fit(X_scaled)

def get_score_and_labels(combinations, X_scaled):
	scores = []
	all_labels_list = []
	labels = db.labels_

	for i, (eps, num_samples) in enumerate(combinations):
		dbscan_cluster_models = DBSCAN(eps = eps, min_samples = num_samples).fit(X_scaled)
		labels = dbscan_cluster_models.labels_
		labels_set = set(labels)
		num_clusters = len(labels_set) 
		if -1 in labels_set:
			num_clusters -= 1

		if (num_clusters < 2):
			scores.append(-10)
			all_labels_list.append('bad')
			c = (eps, num_samples)
			#print(f"combinations{c} on iteration {i + 1} of {N} has {num_clusters} clusters.Move on")
			continue

		scores.append(metrics.silhouette_score(X_scaled,labels))
		all_labels_list.append(labels)
		#print(f" Index: {i}, Score: {scores[-1]}, Numclusters: {num_clusters} ")
	best_index = np.argmax(scores)
	best_parameters = combinations[best_index]
	best_labels = all_labels_list[best_index]
	best_score = scores[best_index]

	return {'best_epsilon': best_parameters[0],'best_min_sample': best_parameters[1], 'best_score': best_score, 'best_labels': best_labels}	
best_dict = get_score_and_labels(combinations, X_scaled)	
print(best_dict)

## Apply DBSCAN 
db = DBSCAN(eps=best_dict['best_epsilon'], min_samples= best_dict['best_min_sample']).fit(X_scaled)
#print('db:', 'Type:',type(db) )

## Visualize the clusters
unique_labels = set(best_dict['best_labels'])
num_clusters = len(unique_labels) - (1 if -1 in unique_labels else 0)

fig = plt.figure(figsize=(8, 6))
colors = ['#000000'] + [plt.cm.tab20(i) for i in range(num_clusters)]
my_cmap = ListedColormap(colors)

# Define boundaries and a norm for the color mapping
bounds = np.arange(-1.5, num_clusters + 0.5,1)
norm = BoundaryNorm(bounds, my_cmap.N)

scatter = plt.scatter(X_scaled[:, 0], X_scaled[:, 1],c = best_dict['best_labels'] ,cmap = my_cmap, norm = norm)

# Create a color bar with ticks and labels at the start of each segment
cbar = plt.colorbar(scatter, ticks=np.arange(-1, num_clusters))
cbar.set_ticklabels(['Noise'] + [f'Cluster {i + 1}' for i in range(num_clusters)])
# Add best silhouette score annotation
best_silhouette = best_dict['best_score']
#plt.annotate(f'Silhouette Score: {best_silhouette:.2f}', xy=(0.03, 0.97), xycoords='axes fraction', fontsize=10, fontweight='bold')

plt.text(-0.15, 1.1, f'Silhouette Score: {best_silhouette:.2f}', ha='left', va='top', transform=plt.gca().transAxes, fontsize= 9, fontweight='bold', bbox={'facecolor': 'yellow', 'alpha': 0.4, 'pad': 10})

plt.title('DBSCAN Clustering', fontsize= 9, fontweight='bold')
plt.xlabel('Annual Income (k$)', fontsize= 9, fontweight='bold' )
plt.ylabel('Spending Score (1-100)', fontsize= 9, fontweight='bold')
plt.show()          

## Visualize the clusters in 3D using Plotly
labels = best_dict['best_labels']
df['Cluster'] = labels

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')



scatter = ax.scatter(
    df_X_scaled['Annual Income (k$)'], 
    df_X_scaled['Spending Score (1-100)'], 
    df_X_scaled['Age'], 
    c=df['Cluster'], 
    cmap='viridis'
)

ax.set_xlabel('Annual Income (k$)')
ax.set_ylabel('Spending Score (1-100)')
ax.set_zlabel('Age')
plt.title('3D Scatter Plot with DBSCAN Clustering')

# Create a color bar
cbar = fig.colorbar(scatter, ax=ax, pad=0.1)
cbar.set_label('Cluster')
plt.show()


## Visualize the clusters in 3D using Plotly
labels = best_dict['best_labels']
df['Cluster'] = labels

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')



scatter = ax.scatter(
    df_X_scaled['Annual Income (k$)'], 
    df_X_scaled['Spending Score (1-100)'], 
    df_X_scaled['Gender'], 
    c=df['Cluster'], 
    cmap='viridis'
)

ax.set_xlabel('Annual Income (k$)')
ax.set_ylabel('Spending Score (1-100)')
ax.set_zlabel('Age')
plt.title('3D Scatter Plot with DBSCAN Clustering')

# Create a color bar
cbar = fig.colorbar(scatter, ax=ax, pad=0.1)
cbar.set_label('Cluster')
plt.show()







#graph matrix
X_scaled_df = pd.DataFrame(X_scaled, columns=['Annual Income (k$)', 'Spending Score (1-100)', 'Gender', 'Age'])

attributes = ["Age", "Gender", "Annual Income (k$)",
              "Spending Score (1-100)"]

scatter_matrix(X_scaled_df, figsize=(12, 8),diagonal='kde', alpha=0.8)
#save_fig("scatter_matrix_plot")  # extra code
#plt.show()









