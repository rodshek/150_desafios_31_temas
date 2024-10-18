import nltk
import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer

# Baixar o vocabulário de sentimentos do NLTK
nltk.download('vader_lexicon')

# Dados fictícios sobre resenhas de produtos
data = {
    'Resenha': [
        'Adorei o produto! Superou minhas expectativas.',
        'O produto chegou com defeito e o atendimento foi ruim.',
        'Muito bom, recomendo a todos.',
        'Não gostei, o produto é de má qualidade.',
        'Excelente, cumpriu o que prometeu.'
    ]
}

# Criar DataFrame
df = pd.DataFrame(data)

# Inicializar o analisador de sentimentos
sia = SentimentIntensityAnalyzer()

# Função para analisar o sentimento


def analisar_sentimento(texto):
    resultado = sia.polarity_scores(texto)
    if resultado['compound'] >= 0.05:
        return 'Positivo'
    elif resultado['compound'] <= -0.05:
        return 'Negativo'
    else:
        return 'Neutro'


# Aplicar a função de análise de sentimento
df['Sentimento'] = df['Resenha'].apply(analisar_sentimento)

# Exibir resultados
print("Resenhas com Análise de Sentimento:")
print(df)
