import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Baixar o recurso necessário do NLTK
nltk.download('vader_lexicon')

# Função para análise de sentimentos


def analyze_sentiment(text):
    # Inicializar o analisador de sentimentos
    sid = SentimentIntensityAnalyzer()

    # Analisar o texto
    sentiment_scores = sid.polarity_scores(text)

    print("Análise de Sentimentos:")
    print(f"Texto: {text}")
    print(f"Pontuação de Sentimento: {sentiment_scores}")


if __name__ == '__main__':
    sample_text = "I love programming in Python. It's amazing how powerful and flexible it is!"
    analyze_sentiment(sample_text)
