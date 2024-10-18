import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# Dados fictícios sobre imóveis
data = {
    'Tamanho': [50, 60, 70, 80, 90, 100, 110, 120, 130, 140],
    'Quartos': [1, 2, 2, 3, 3, 4, 4, 5, 5, 6],
    'Preço': [150000, 180000, 200000, 220000, 240000, 260000, 280000, 300000, 320000, 340000]
}

# Criar DataFrame
df = pd.DataFrame(data)

# Definir variáveis independentes (X) e dependentes (y)
X = df[['Tamanho', 'Quartos']]
y = df['Preço']

# Dividir os dados em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0)

# Criar e treinar o modelo de regressão linear
model = LinearRegression()
model.fit(X_train, y_train)

# Fazer previsões no conjunto de teste
y_pred = model.predict(X_test)

# Avaliar o modelo
mse = mean_squared_error(y_test, y_pred)
print(f"Erro Quadrático Médio (MSE): {mse}")

# Mostrar coeficientes do modelo
print(f"Coeficientes: {model.coef_}")
print(f"Intercepto: {model.intercept_}")

# Fazer uma previsão com dados fictícios
novo_imovel = np.array([[100, 3]])
previsao_preco = model.predict(novo_imovel)
print(
    f"Preço previsto para o imóvel de 100m² e 3 quartos: {previsao_preco[0]}")
