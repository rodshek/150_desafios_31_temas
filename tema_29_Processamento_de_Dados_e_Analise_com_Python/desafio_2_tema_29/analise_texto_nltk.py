import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Texto de exemplo para análise
texto = """
O Python é uma linguagem de programação extremamente popular e poderosa. 
Ele é amplamente utilizado em ciência de dados, desenvolvimento web e automação. 
A simplicidade da sintaxe e a ampla gama de bibliotecas disponíveis tornam o Python uma escolha excelente para novos programadores e profissionais experientes.
"""

# Inicialização do analisador de sentimentos
analisador = SentimentIntensityAnalyzer()

# Análise de sentimentos
pontuacao = analisador.polarity_scores(texto)

# Resultados
print(f"Texto: {texto}")
print(f"Pontuação de Sentimentos: {pontuacao}")
