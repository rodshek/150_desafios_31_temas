import os

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from dotenv import load_dotenv
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

# Carregar o conjunto de dados Iris
data = load_iris()
X = data.data
y = data.target

# Escalonar os dados
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Aplicar o algoritmo KMeans
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(X_scaled)

# Avaliar a qualidade da clusterização
silhouette_avg = silhouette_score(X_scaled, clusters)
print(f"Silhouette Score: {silhouette_avg:.2f}")

# Visualizar os clusters
plt.figure(figsize=(10, 6))
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=clusters,
            cmap='viridis', marker='o', edgecolor='k', s=50)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[
            :, 1], s=200, c='red', marker='x')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('KMeans Clustering of Iris Dataset')
plt.colorbar(label='Cluster Label')
plt.show()


# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Acessar as variáveis de ambiente
n_clusters = int(os.getenv('N_CLUSTERS', 3))

# Aplicar o algoritmo KMeans
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
clusters = kmeans.fit_predict(X_scaled)
