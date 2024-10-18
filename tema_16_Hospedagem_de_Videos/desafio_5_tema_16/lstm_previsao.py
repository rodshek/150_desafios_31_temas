import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.models import Sequential


# Gerar dados sintéticos para o exemplo
def gerar_dados(n_samples=100):
    """Gera dados sintéticos de séries temporais com uma tendência sazonal."""
    np.random.seed(0)
    x = np.arange(n_samples)
    y = np.sin(0.1 * x) + 0.1 * np.random.randn(n_samples)  # Sinal com ruído
    return x, y


def preparar_dados(y, n_steps=10):
    """Prepara os dados para treinamento do modelo LSTM."""
    X, Y = [], []
    for i in range(len(y) - n_steps):
        X.append(y[i:i + n_steps])
        Y.append(y[i + n_steps])
    return np.array(X), np.array(Y)


def construir_modelo(input_shape):
    """Constrói e compila o modelo LSTM."""
    modelo = Sequential([
        LSTM(50, activation='relu', input_shape=input_shape),
        Dense(1)
    ])

    modelo.compile(optimizer='adam', loss='mse')
    return modelo


def plotar_resultados(y_true, y_pred):
    """Plota os resultados da previsão."""
    plt.figure(figsize=(12, 6))
    plt.plot(y_true, label='Dados Reais')
    plt.plot(np.arange(len(y_true) - len(y_pred), len(y_true)),
             y_pred, label='Previsões', color='red')
    plt.xlabel('Tempo')
    plt.ylabel('Valor')
    plt.legend()
    plt.show()


def main():
    # Gerar dados
    x, y = gerar_dados()

    # Normalizar os dados
    scaler = MinMaxScaler()
    y = scaler.fit_transform(y.reshape(-1, 1)).flatten()

    # Preparar os dados
    n_steps = 10
    X, Y = preparar_dados(y, n_steps)

    # Redimensionar para o formato [amostras, timesteps, características]
    X = X.reshape((X.shape[0], X.shape[1], 1))
    input_shape = (X.shape[1], X.shape[2])

    # Construir e treinar o modelo
    modelo = construir_modelo(input_shape)
    modelo.fit(X, Y, epochs=200, verbose=0)

    # Fazer previsões
    y_pred = modelo.predict(X)

    # Inverter a normalização para obter os valores reais
    y_true = scaler.inverse_transform(Y.reshape(-1, 1)).flatten()
    y_pred = scaler.inverse_transform(y_pred).flatten()

    # Plotar os resultados
    plotar_resultados(np.concatenate((np.full(n_steps, np.nan), y_true)),
                      np.concatenate((np.full(n_steps, np.nan), y_pred)))


if __name__ == '__main__':
    main()
