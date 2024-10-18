import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.utils import to_categorical

# Definir parâmetros
num_classes = 10
epochs = 10

# Carregar o conjunto de dados CIFAR-10
(X_train, y_train), (X_test, y_test) = cifar10.load_data()

# Normalizar os dados
X_train, X_test = X_train / 255.0, X_test / 255.0

# Codificar as etiquetas
y_train = to_categorical(y_train, num_classes)
y_test = to_categorical(y_test, num_classes)

# Construir o modelo CNN
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(num_classes, activation='softmax')
])

# Compilar o modelo
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Treinar o modelo
model.fit(X_train, y_train, epochs=epochs, batch_size=64, validation_split=0.2)

# Avaliar o modelo
test_loss, test_acc = model.evaluate(X_test, y_test)
print(f'\nAcurácia no conjunto de teste: {test_acc:.2f}')
