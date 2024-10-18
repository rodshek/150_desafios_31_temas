import nltk
import pandas as pd
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

# Baixar recursos do NLTK
nltk.download('stopwords')

# Dados fictícios sobre e-mails
data = {
    'Texto': [
        'Oferta especial para você! Ganhe dinheiro rápido.',
        'Reunião agendada para amanhã às 10h.',
        'Parabéns! Você ganhou um prêmio.',
        'Por favor, confirme sua presença no evento.',
        'Aproveite a promoção de 50% de desconto.',
        'Seu extrato bancário está disponível.',
        'Compra confirmada. Agradecemos pela preferência.',
        'Novo curso disponível para você.'
    ],
    'Classe': ['Spam', 'Não Spam', 'Spam', 'Não Spam', 'Spam', 'Não Spam', 'Não Spam', 'Não Spam']
}

# Criar DataFrame
df = pd.DataFrame(data)

# Pré-processamento dos dados
stop_words = stopwords.words('portuguese')
vectorizer = CountVectorizer(stop_words=stop_words)
X = vectorizer.fit_transform(df['Texto'])
y = df['Classe']

# Dividir os dados em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0)

# Criar e treinar o modelo Naive Bayes
model = MultinomialNB()
model.fit(X_train, y_train)

# Fazer previsões no conjunto de teste
y_pred = model.predict(X_test)

# Avaliar o modelo
print("Relatório de Classificação:")
print(classification_report(y_test, y_pred))

# Fazer uma previsão com dados fictícios
novo_email = ["Ganhe dinheiro com essa oferta imperdível"]
novo_email_vectorizado = vectorizer.transform(novo_email)
previsao_classe = model.predict(novo_email_vectorizado)
print(f"\nClassificação para o novo e-mail: {previsao_classe[0]}")
