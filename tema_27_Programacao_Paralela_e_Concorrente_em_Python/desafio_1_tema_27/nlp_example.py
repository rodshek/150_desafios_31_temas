import string

import nltk
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.tokenize import sent_tokenize, word_tokenize

# Baixar recursos do NLTK
nltk.download('punkt')
nltk.download('stopwords')

# Função para processamento de texto


def process_text(text):
    # Tokenizar o texto em sentenças
    sentences = sent_tokenize(text)
    print("Sentenças:", sentences)

    # Tokenizar o texto em palavras
    words = word_tokenize(text)
    print("Palavras:", words)

    # Remover pontuações e palavras de parada
    words = [word.lower() for word in words if word.isalpha()]
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word not in stop_words]
    print("Palavras filtradas:", filtered_words)

    # Frequência das palavras
    freq_dist = FreqDist(filtered_words)
    print("Frequência das palavras:", freq_dist.most_common())


if __name__ == '__main__':
    sample_text = """Natural language processing (NLP) is a sub-field of artificial intelligence (AI) that deals with the interaction between computers and humans through natural language. The ultimate objective of NLP is to enable computers to understand, interpret, and generate human language in a way that is both valuable and meaningful."""
    process_text(sample_text)
