from textblob import TextBlob

# Texto de exemplo para análise
texto = """
O Python é uma linguagem de programação extremamente popular e poderosa. 
Ele é amplamente utilizado em ciência de dados, desenvolvimento web e automação. 
A simplicidade da sintaxe e a ampla gama de bibliotecas disponíveis tornam o Python uma escolha excelente para novos programadores e profissionais experientes.
"""

# Criação do objeto TextBlob
blob = TextBlob(texto)

# Análise de sentimentos
sentimento = blob.sentiment

# Resultados
print(f"Texto: {texto}")
print(f"Polaridade: {sentimento.polarity}")
print(f"Subjetividade: {sentimento.subjectivity}")
