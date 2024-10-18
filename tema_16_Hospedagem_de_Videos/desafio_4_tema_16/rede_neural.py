import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models


def carregar_dados():
    """Carrega o conjunto de dados MNIST e o prepara para treinamento e teste."""
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

    # Normaliza os dados
    x_train, x_test = x_train / 255.0, x_test / 255.0

    # Expande as dimensões para adicionar a dimensão do canal (grayscale)
    x_train = np.expand_dims(x_train, -1)
    x_test = np.expand_dims(x_test, -1)

    return (x_train, y_train), (x_test, y_test)


def construir_modelo():
    """Constrói e compila o modelo de rede neural."""
    modelo = models.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dense(10, activation='softmax')
    ])

    modelo.compile(optimizer='adam',
                   loss='sparse_categorical_crossentropy',
                   metrics=['accuracy'])

    return modelo


def treinar_modelo(modelo, x_train, y_train):
    """Treina o modelo com os dados de treinamento."""
    historico = modelo.fit(x_train, y_train, epochs=5, validation_split=0.2)
    return historico


def avaliar_modelo(modelo, x_test, y_test):
    """Avalia o desempenho do modelo e exibe as métricas."""
    teste_loss, teste_acc = modelo.evaluate(x_test, y_test, verbose=2)
    print(f'\nAcurácia no conjunto de teste: {teste_acc:.4f}')

    # Plota a perda e a acurácia durante o treinamento
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.plot(historico.history['loss'], label='Loss de Treinamento')
    plt.plot(historico.history['val_loss'], label='Loss de Validação')
    plt.xlabel('Época')
    plt.ylabel('Loss')
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(historico.history['accuracy'], label='Acurácia de Treinamento')
    plt.plot(historico.history['val_accuracy'], label='Acurácia de Validação')
    plt.xlabel('Época')
    plt.ylabel('Acurácia')
    plt.legend()

    plt.show()


def main():
    """Função principal para executar o script."""
    (x_train, y_train), (x_test, y_test) = carregar_dados()
    modelo = construir_modelo()
    historico = treinar_modelo(modelo, x_train, y_train)
    avaliar_modelo(modelo, x_test, y_test)


if __name__ == '__main__':
    main()
