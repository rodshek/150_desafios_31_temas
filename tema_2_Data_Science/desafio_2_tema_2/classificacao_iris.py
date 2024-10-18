import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Carregar o conjunto de dados Iris
iris = load_iris()
X = iris.data
y = iris.target
feature_names = iris.feature_names
target_names = iris.target_names

# Criar DataFrame
df = pd.DataFrame(data=X, columns=feature_names)
df['target'] = y

# Dividir os dados em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0)

# Criar e treinar o modelo K-Nearest Neighbors (KNN)
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

# Fazer previsões
y_pred = model.predict(X_test)

# Avaliar o modelo
print("Relatório de Classificação:")
print(classification_report(y_test, y_pred, target_names=target_names))

# Visualizar dados de teste e previsões
plt.figure(figsize=(12, 6))
sns.scatterplot(x=X_test[:, 2], y=X_test[:, 3], hue=y_pred,
                palette='viridis', marker='o', legend='full')
plt.xlabel('Comprimento da Pétala')
plt.ylabel('Largura da Pétala')
plt.title('Classificação de Flores Iris com KNN')
plt.show()
