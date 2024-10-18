import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split

# Carregar o conjunto de dados MNIST
mnist = fetch_openml('mnist_784')

# Dividir os dados e os rótulos
X, y = mnist.data, mnist.target

# Dividir os dados em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0)

# Criar e treinar o modelo de Regressão Logística
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Fazer previsões
y_pred = model.predict(X_test)

# Avaliar o modelo
accuracy = accuracy_score(y_test, y_pred)
print(f"Acurácia: {accuracy}")
print("Relatório de Classificação:")
print(classification_report(y_test, y_pred))

# Visualizar algumas imagens e suas previsões
fig, axes = plt.subplots(1, 5, figsize=(10, 3))
for ax, image, label in zip(axes, X_test[:5].values, y_pred[:5]):
    ax.imshow(np.reshape(image, (28, 28)), cmap='gray')
    ax.set_title(f'Predito: {label}')
    ax.axis('off')
plt.show()
