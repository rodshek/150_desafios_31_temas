import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# Dados fictícios sobre casas
data = {
    'Tamanho': [1000, 1500, 2000, 2500, 3000],
    'Preço': [300000, 400000, 500000, 600000, 700000]
}

# Criar DataFrame
df = pd.DataFrame(data)

# Definir variáveis independentes e dependentes
X = df[['Tamanho']]
y = df['Preço']

# Dividir os dados em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0)

# Criar e treinar o modelo de regressão linear
model = LinearRegression()
model.fit(X_train, y_train)

# Fazer previsões
y_pred = model.predict(X_test)

# Avaliar o modelo
mse = mean_squared_error(y_test, y_pred)
print(f"Erro Quadrático Médio (MSE): {mse}")

# Visualizar resultados
plt.scatter(X, y, color='blue', label='Dados reais')
plt.plot(X, model.predict(X), color='red',
         linewidth=2, label='Linha de Regressão')
plt.xlabel('Tamanho (em pés quadrados)')
plt.ylabel('Preço (em dólares)')
plt.title('Regressão Linear - Preço das Casas')
plt.legend()
plt.show()
