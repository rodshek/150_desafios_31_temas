import string

import nltk
import pandas as pd
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# Baixar stopwords do NLTK
nltk.download('stopwords')

# Dados fictícios sobre notícias
data = {
    'texto': [
        'A empresa XYZ lançou um novo produto hoje.',
        'A ação da empresa ABC caiu devido à crise econômica.',
        'A nova tecnologia vai revolucionar o setor de saúde.',
        'Os esportes estão em alta esta temporada.',
        'O mercado de trabalho está crescendo rapidamente.'
    ],
    'categoria': [
        'Negócios',
        'Negócios',
        'Tecnologia',
        'Esportes',
        'Trabalho'
    ]
}

# Criar DataFrame
df = pd.DataFrame(data)

# Pré-processamento de texto


def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = ' '.join([word for word in text.split()
                    if word not in stopwords.words('english')])
    return text


df['texto'] = df['texto'].apply(preprocess_text)

# Definir variáveis independentes e dependentes
X = df['texto']
y = df['categoria']

# Dividir os dados em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0)

# Criar um pipeline com TF-IDF e Naive Bayes
model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(X_train, y_train)

# Fazer previsões
y_pred = model.predict(X_test)

# Avaliar o modelo
print("Relatório de Classificação:")
print(classification_report(y_test, y_pred))
