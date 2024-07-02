import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np 
from itertools import combinations

from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
from sklearn import metrics
#from scipy.spatial.distance import cdist

###Data Loading:
## Get the data
dfwithna = pd.read_csv('Mall_Customers.csv')
#print('Number of raws before dropping nan value',len(dfwithna))

## Drop rows with any missing values
df = dfwithna.dropna()
#print('Number of raws after dropping nan value',len(df))

##Data Type Conversion and Mapping categorical variables
df["Age"]= df["Age"].astype(np.int64)
df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1})
df['Gender']= df["Gender"].astype(np.int64)

## Selecting features for clustering
X = df[['Annual Income (k$)', 'Spending Score (1-100)','Gender' ,'Age']]

def KMeans_features(X):
    ## Normalize the data
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)
    ## number of rows and number of columns
    num_rows, num_cols = X_scaled.shape
    print(f"Number of rows:{num_rows}, Number of columns:{num_cols}")

    column_names = X.columns.tolist()
    column_name_map = {i: column_names[i] for i in range(num_cols)}  # Map column index to column name


    for combination_length in range(2 ,num_cols + 1 ):
        for combo in combinations(range(num_cols), combination_length):
            combo_names = [column_name_map[i] for i in combo]
            combo_str = ', '.join(combo_names)
            print(combo_names)
            #print('X Features after normalize:',len((X_scaled)[:,i]))
            data = X_scaled[:,combo]
            #print(f'Combination of {combo}:\n{data}\n')
            combo_str = ', '.join([str(c) for c in combo])
            #print(f"Combination of columns {combo_str}:\n{data}\n")
            #df_X_scaled = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)
            #print(df_X_scaled.columns)

            inertias = [] #?
            silhouette_scores = [] #?
            max_silhouette_score = -1  # Initialize to a very low value

            for i in range(2,20):
                kmeans = KMeans(n_clusters=i, random_state=42)#?
                kmeans.fit(data)
                inertias.append(kmeans.inertia_)

                # Calculate silhouette score
                score = metrics.silhouette_score(data, kmeans.labels_)
                silhouette_scores.append(score)
                #print(f"Number of clusters: {i}, Silhouette Score: {score}")
                if score > max_silhouette_score:
                    max_silhouette_score = score  # Update max silhouette score
                    max_score_for_num_cluster = i
                print(f"Number of clusters: {i}, Silhouette Score: {score}")
            print(f"Max Silhouette Score for combination {combo_str}: {max_silhouette_score}, Number of clusters: {max_score_for_num_cluster} ")        


        # Plot elbow method
            plt.figure(figsize=(14, 7))

            plt.subplot(1, 2, 1)
            plt.plot(range(2, 20), inertias, marker='o')
            plt.title('Elbow Method')
            plt.xlabel('Number of clusters')
            plt.ylabel('Inertia')
            plt.xticks(range(2, 20, 2))  # Set x-axis ticks with a specific interval

            # Plot silhouette scores
            plt.subplot(1, 2, 2)
            plt.plot(range(2, 20), silhouette_scores, marker='o', color='r')
            plt.title('Silhouette Scores')
            plt.xlabel('Number of clusters')
            plt.ylabel('Silhouette Score')
            plt.xticks(range(2, 20, 2))  # Set x-axis ticks with a specific interval

            # Add combination name as a text box
            plt.text(0.05, 0.95, f"Features: {combo_names}", verticalalignment='top', horizontalalignment='left',
                     transform=plt.gca().transAxes, color='black', fontsize=8, weight='bold', 
                     bbox=dict(facecolor='yellow', alpha=0.3))

            # Add text with the maximum silhouette score and number of clusters
            textstr = f"Max Silhouette Score: {max_silhouette_score:.3f}\nNumber of clusters: {max_score_for_num_cluster}"
            plt.text(0.95, 0.01, textstr, verticalalignment='bottom', horizontalalignment='right',
                transform=plt.gca().transAxes, color='black', fontsize=12,
                bbox=dict(facecolor='white', alpha=0.5))
            


            plt.tight_layout(rect=[0, 0.03, 1, 0.95])    
            plt.show()
    

KMeans_features(X)