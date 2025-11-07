import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, DBSCAN
from sklearn.metrics import confusion_matrix




def section1_kmeans(iris):
    print("\n=== SECTION 1: K-MEANS CLUSTERING ===\n")


# 1. Load the Iris dataset and display first five rows, shape, and feature names
X = iris.data
feature_names = iris.feature_names
df = pd.DataFrame(X, columns=feature_names)
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)


print("First 5 rows:")
print(df.head())
print(f"Shape: {df.shape}")
print(f"Feature names: {feature_names}\n")


# 2. Standardize the feature columns
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df[feature_names])
df_scaled = pd.DataFrame(X_scaled, columns=feature_names)
print("Standardized data (first 5 rows):")
print(df_scaled.head())


# 3. Apply K-Means clustering with n_clusters=3 and add predicted labels
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans_labels = kmeans.fit_predict(X_scaled)
df['kmeans_cluster'] = kmeans_labels
print("\nK-Means clustering completed. Cluster counts:")
print(df['kmeans_cluster'].value_counts().sort_index())
print("Cluster centers (scaled feature space):")
centers_df = pd.DataFrame(kmeans.cluster_centers_, columns=feature_names)
print(centers_df)
print(f"Inertia: {kmeans.inertia_}\n")


# 4. Scatter plot: SepalLength vs SepalWidth colored by cluster label
plt.figure(figsize=(7, 5))
plt.scatter(df[feature_names[0]], df[feature_names[1]], c=df['kmeans_cluster'], cmap='viridis')
plt.xlabel(feature_names[0])
plt.ylabel(feature_names[1])
plt.title('K-Means: Sepal Length vs Sepal Width (k=3)')
plt.grid(True)
plt.show()


# 5. Elbow method (inertia) for k = 1..10
inertias = []
ks = range(1, 11)
for k in ks:
km = KMeans(n_clusters=k, random_state=42, n_init=10)
km.fit(X_scaled)
inertias.append(km.inertia_)


plt.figure(figsize=(7, 5))
plt.plot(list(ks), inertias, marker='o')
plt.xticks(ks)
plt.xlabel('Number of clusters k')
plt.ylabel('Inertia')
plt.title('Elbow Method: Inertia vs k')
return df, X_scaled