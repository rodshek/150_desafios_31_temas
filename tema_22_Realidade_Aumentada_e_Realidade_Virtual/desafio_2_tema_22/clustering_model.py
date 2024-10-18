import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler

# Carregar o conjunto de dados Iris
data = load_iris()
X = data.data

# Normalizar os dados
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Inicializar o modelo KMeans com 3 clusters
kmeans = KMeans(n_clusters=3, random_state=42)

# Treinar o modelo
kmeans.fit(X_scaled)

# Obter as previsões de cluster
y_kmeans = kmeans.predict(X_scaled)

# Plotar os resultados
plt.figure(figsize=(8, 6))
plt.scatter(X_scaled[:, 0], X_scaled[:, 1],
            c=y_kmeans, cmap='viridis', marker='o')
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='red',
            s=200, alpha=0.75, marker='x')
plt.title('K-Means Clustering')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()
