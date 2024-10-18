import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


def carregar_dados(caminho_arquivo):
    """Carrega os dados do arquivo CSV em um DataFrame do pandas."""
    return pd.read_csv(caminho_arquivo)


def preparar_dados(df):
    """Prepara os dados para treinamento e teste do modelo."""
    X = df.drop(columns=['target'])
    y = df['target']
    return train_test_split(X, y, test_size=0.2, random_state=42)


def treinar_modelo(X_train, y_train):
    """Treina o modelo de regressão linear."""
    modelo = LinearRegression()
    modelo.fit(X_train, y_train)
    return modelo


def avaliar_modelo(modelo, X_test, y_test):
    """Avalia o desempenho do modelo e exibe as métricas."""
    y_pred = modelo.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"Mean Squared Error: {mse:.2f}")
    print(f"R² Score: {r2:.2f}")

    plt.figure(figsize=(10, 6))
    plt.scatter(y_test, y_pred, color='blue')
    plt.plot([min(y_test), max(y_test)], [min(y_test),
             max(y_test)], color='red', linestyle='--')
    plt.xlabel('Valores Reais')
    plt.ylabel('Valores Preditos')
    plt.title('Valores Reais vs. Valores Preditos')
    plt.show()


def main():
    """Função principal para executar o script."""
    caminho_arquivo = 'dados.csv'  # Substitua pelo caminho do seu arquivo CSV
    df = carregar_dados(caminho_arquivo)

    X_train, X_test, y_train, y_test = preparar_dados(df)
    modelo = treinar_modelo(X_train, y_train)
    avaliar_modelo(modelo, X_test, y_test)


if __name__ == '__main__':
    main()
