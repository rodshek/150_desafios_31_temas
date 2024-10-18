from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split


def main():
    # Carregar o conjunto de dados Iris
    data = load_iris()
    X = data.data
    y = data.target

    # Dividir o conjunto de dados em conjuntos de treino e teste
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42)

    # Criar e treinar o modelo
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)

    # Fazer previsões
    y_pred = model.predict(X_test)

    # Avaliar o modelo
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    # Exibir resultados
    print(f'Accuracy: {accuracy:.2f}')
    print('Classification Report:')
    print(report)


if __name__ == "__main__":
    main()
