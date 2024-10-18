import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Definir parâmetros
vocab_size = 10000
maxlen = 500
embedding_dim = 16
epochs = 5

# Carregar o conjunto de dados IMDB
(X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=vocab_size)

# Padronizar o comprimento das sequências
X_train = pad_sequences(X_train, maxlen=maxlen)
X_test = pad_sequences(X_test, maxlen=maxlen)

# Construir o modelo RNN
model = models.Sequential([
    layers.Embedding(input_dim=vocab_size,
                     output_dim=embedding_dim, input_length=maxlen),
    layers.SimpleRNN(32, return_sequences=True),
    layers.GlobalAveragePooling1D(),
    layers.Dense(1, activation='sigmoid')
])

# Compilar o modelo
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Treinar o modelo
model.fit(X_train, y_train, epochs=epochs, batch_size=64, validation_split=0.2)

# Avaliar o modelo
test_loss, test_acc = model.evaluate(X_test, y_test)
print(f'\nAcurácia no conjunto de teste: {test_acc:.2f}')
