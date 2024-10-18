import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans

# Dados fictícios sobre clientes
data = {
    'Idade': [25, 45, 35, 50, 23, 37, 40, 60, 52, 29],
    'Renda': [50000, 60000, 55000, 70000, 40000, 65000, 62000, 75000, 68000, 47000]
}

# Criar DataFrame
df = pd.DataFrame(data)

# Definir variáveis independentes
X = df[['Idade', 'Renda']]

# Aplicar K-means clustering
kmeans = KMeans(n_clusters=3, random_state=0)
df['Cluster'] = kmeans.fit_predict(X)

# Exibir resultados
print("Centros dos clusters:")
print(kmeans.cluster_centers_)
print("\nDados com os clusters atribuídos:")
print(df)

# Visualização dos clusters
plt.scatter(df['Idade'], df['Renda'], c=df['Cluster'], cmap='viridis')
plt.xlabel('Idade')
plt.ylabel('Renda')
plt.title('Segmentação de Clientes - K-means Clustering')
plt.colorbar(label='Cluster')
plt.show()
