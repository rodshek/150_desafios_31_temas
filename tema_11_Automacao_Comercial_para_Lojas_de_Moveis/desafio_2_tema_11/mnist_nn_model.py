import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import layers, models


def main():
    # Carregar o conjunto de dados MNIST
    mnist = tf.keras.datasets.mnist
    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    # Normalizar os dados
    x_train, x_test = x_train / 255.0, x_test / 255.0

    # Construir o modelo
    model = models.Sequential([
        layers.Flatten(input_shape=(28, 28)),
        layers.Dense(128, activation='relu'),
        layers.Dropout(0.2),
        layers.Dense(10, activation='softmax')
    ])

    # Compilar o modelo
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    # Treinar o modelo
    history = model.fit(x_train, y_train, epochs=5,
                        validation_data=(x_test, y_test))

    # Avaliar o modelo
    test_loss, test_acc = model.evaluate(x_test, y_test)
    print(f'Test accuracy: {test_acc:.2f}')

    # Plotar a acurácia do treinamento
    plt.plot(history.history['accuracy'], label='accuracy')
    plt.plot(history.history['val_accuracy'], label='val_accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.ylim([0, 1])
    plt.legend(loc='lower right')
    plt.show()


if __name__ == "__main__":
    main()
