import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np 
import itertools



from sklearn import metrics
from sklearn.cluster import DBSCAN
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import adjusted_rand_score
#from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import ParameterGrid

## Get the data
dfwithna = pd.read_csv('Mall_Customers.csv')
#print('Number of raws before dropping nan value',len(dfwithna))

## print all features
print('Features:',dfwithna.columns)

## Drop rows with any missing values
df = dfwithna.dropna()
#print('Number of raws after dropping nan value',len(df))

## Select two features for clustering
X = df[['Annual Income (k$)', 'Spending Score (1-100)']]
#print('Max Annual Income',max(X.iloc[:,0]),'Min Annual Income:',min(X.iloc[:,0]))
#print('Max Spending Score',max(X.iloc[:,1]),'Min Spending Score:',min(X.iloc[:,1]))

# normalize the data
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)
#print('X two Features after normalize:', X_scaled)



## Grid search
epsilons = np.linspace(0.001,1, num = 1000)
#print(epsilons)
min_samples = np.arange(2,200, step = 2)
#print(min_samples)

combinations = list(itertools.product(epsilons, min_samples))
#print(combinations) 
N = len(combinations)
print(N)



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
		print(f" Index: {i}, Score: {scores[-1]}, Numclusters: {num_clusters} ")
	best_index = np.argmax(scores)
	best_parameters = combinations[best_index]
	best_labels = all_labels_list[best_index]
	best_score = scores[best_index]

	return {'best_epsilon': best_parameters[0],'best_min_sample': best_parameters[1], 'best_score': best_score}	
best_dict = get_score_and_labels(combinations, X_scaled)	
print(best_dict)			

df['cluster'] = best_dict




#eps k-distance graph; ,MinPts >= D+1 , D = dimensions od data, at least 3, MinPts = 2·D  
# Compute the distances to the kth nearest neighbor
k = 3 # Choose the value of k,  k=MinPts-1
# creating an object of the NearestNeighbors class
neighb = NearestNeighbors(n_neighbors=k)
#print('neighb:', neighb)
# fitting the data to the object
nbrs=neighb.fit(X_scaled)
#print('nbrs:', nbrs)
# finding the nearest neighbours
distances, indices = nbrs.kneighbors(X_scaled)
#print(distances)
#print(indices)

# Sort distances and select the kth nearest neighbor distance for each point
# sorting the distances
distances = np.sort(distances, axis = 0)
#print(distances)

# Plot the k-distance graph
plt.figure(figsize=(10, 6))
plt.plot(range(1, len(distances) + 1), distances, marker='o', linestyle='-')
plt.title('k-Distance Graph')
plt.xlabel('Data Point Index')
plt.ylabel(f'{k}-Distance')
plt.grid(True)
#plt.show()


# Find the knee point (change in slope)
#diff = np.diff(k_distances, 2)
#knee_point = np.argmax(diff) + 2  # Add 2 because of the way we calculated differences
#plt.axvline(x=knee_point, color='r', linestyle='--', label='Knee Point')
#plt.legend()
#plt.show()
#print("Number of clusters suggested by knee point method:", knee_point)


## Apply DBSCAN 
db = DBSCAN(eps=0.09, min_samples=4).fit(X_scaled)
#print('db:', 'Type:',type(db) )

#core points indices
#print('Number of core points out of 200 data points:',len(db.core_sample_indices_))
#print('core points index:',db.core_sample_indices_)
#print('core data points:',db.components_)


## db.labels_ is an array that contains the cluster labels for each point in the datas
core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
#print('core_samples_mask:', 'Type:',type(core_samples_mask),'ndimension:', core_samples_mask.ndim )
core_samples_mask[db.core_sample_indices_] = True
#print(core_samples_mask[db.core_sample_indices_] )

# Extract cluster labels
labels = db.labels_
# add a column to data set with the label of clusters
df['cluster'] = db.labels_
print(df['cluster'].value_counts())
# Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
#print('n_clusters_:',n_clusters_)
# Fit the model
db.fit(X_scaled)

##plot result
# Black removed and is used for noise instead.
unique_labels = set(labels)
#print(unique_labels)
colors = ['y', 'b', 'g', 'r','khaki','gray', 'olive' , 'purple', 'orange', 'cyan', 'pink', 'brown','lime']
#print(colors)
for k, col in zip(unique_labels, colors):
	#print(k,col)
	if k == -1:
		# Black used for noise.
		col = 'k'
	class_member_mask = (labels == k)
	xy = X_scaled[class_member_mask & core_samples_mask]
	plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col, markeredgecolor='k',markersize=6)

	xy = X_scaled[class_member_mask & ~core_samples_mask]
	plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col, markeredgecolor='k',markersize=6)	

plt.title('number of clusters: %d' % n_clusters_)
plt.show()            		


# evaluation metrics
sc = metrics.silhouette_score(X_scaled, labels)
#print("Silhouette Coefficient:%0.2f" % sc)
#ari = adjusted_rand_score(xy[:, 1], labels)
#print("Adjusted Rand Index: %0.2f" % ari)





# Visualize the clusters
plt.figure(figsize=(10, 6))
plt.scatter(X.iloc[:, 0], X.iloc[:, 1], c=labels, cmap='viridis', s=50, alpha=0.8)

#plt.scatter(iloc.X[:, 0], iloc.X[:, 1], c=labels, cmap='viridis', s=50, alpha=0.8)
plt.title('DBSCAN Clustering')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.colorbar(label='Cluster Label')
plt.show()





