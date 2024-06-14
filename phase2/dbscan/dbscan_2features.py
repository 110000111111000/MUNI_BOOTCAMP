import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np 
import itertools

from matplotlib.colors import ListedColormap
from sklearn import metrics
from sklearn.cluster import DBSCAN
#from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler

#from sklearn.model_selection import GridSearchCV
#from sklearn.metrics import adjusted_rand_score
#from sklearn.model_selection import ParameterGrid

## Get the data
dfwithna = pd.read_csv('Mall_Customers.csv')
#print('Number of raws before dropping nan value',len(dfwithna))

## Drop rows with any missing values
df = dfwithna.dropna()
#print('Number of raws after dropping nan value',len(df))

## Select two features for clustering
X = df[['Annual Income (k$)', 'Spending Score (1-100)']]

## Normalize the data
scaler = MinMaxScaler()
#scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
#print('X two Features after normalize:', X_scaled)

## Grid search
epsilons = np.linspace(0.01,0.1, num = 1000)
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

	return {'best_epsilon': best_parameters[0],'best_min_sample': best_parameters[1], 'best_score': best_score, 'best_labels': best_labels }	
best_dict = get_score_and_labels(combinations, X_scaled)	
print(best_dict)

## Visualize the clusters
## db.labels_ is an array that contains the cluster labels for each point in the datas
#labels = db.labels_
fig = plt.figure(figsize=(10, 6))
# Determine the number of unique clusters, excluding noise (-1)
unique_labels = set(best_dict['best_labels'])
#print(unique_labels) 
num_clusters = len(unique_labels)

colors = plt.cm.tab20(np.linspace(0, 1, num_clusters))
my_cmap = ListedColormap(colors, name="my_cmap")
#-- define some levels and labels
levels  =  [1, 2, 5, 10, 50, 100, 200, 500, 1000, 2000]
labels  =  ['noise','1','2','3','4','5','6','>500','>1000','>2000']
cax = fig.add_axes([0.05, 0.5, 0.9, 0.08],        #-- [x, y, width, height]
                    autoscalex_on=True)

plt.scatter(X.iloc[:, 0], X.iloc[:, 1], c= best_dict['best_labels'], cmap=my_cmap, s=50, alpha=0.8)

# Create a color bar with the appropriate labels
cbar = plt.colorbar(cax,cmap=my_cmap, format='%d')
cbar.set_label('Cluster Label')
cbar.set_ticks(range(-1,num_clusters-1))
cbar.set_ticklabels(range(-1,num_clusters-1))

#colors = ["#000000","#b3a178", "#a1dab4", "#41b6c4", "#2c7fb8", "#253494", "#142060"]
#my_cmap = ListedColormap(colors[:num_clusters+1], name="my_cmap")
#plt.scatter(X.iloc[:, 0], X.iloc[:, 1], c= best_dict['best_labels'], cmap=my_cmap, s=50, alpha=0.8)




#plt.scatter(iloc.X[:, 0], iloc.X[:, 1], c=labels, cmap='viridis', s=50, alpha=0.8)
plt.title('DBSCAN Clustering')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
#plt.colorbar(label='Cluster Label')
plt.show()     










