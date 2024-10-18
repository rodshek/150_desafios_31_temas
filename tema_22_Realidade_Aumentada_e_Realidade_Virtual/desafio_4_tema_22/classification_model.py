import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Gerar um conjunto de dados de classificação
X, y = make_classification(n_samples=100, n_features=2,
                           n_classes=2, n_clusters_per_class=1, random_state=42)

# Escalonar os dados
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Dividir os dados em conjunto de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42)

# Inicializar e treinar o modelo de regressão logística
model = LogisticRegression()
model.fit(X_train, y_train)

# Fazer previsões
y_pred = model.predict(X_test)

# Avaliar o modelo
print("Classification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

# Visualizar os resultados
plt.figure(figsize=(8, 6))
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap='coolwarm',
            marker='o', edgecolor='k', s=100, label='Dados Reais')
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_pred, cmap='coolwarm',
            marker='x', edgecolor='k', s=100, label='Previsões')
plt.title('Classificação com Regressão Logística')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.show()
