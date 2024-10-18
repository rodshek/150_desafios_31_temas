import string
from collections import Counter

import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Baixar recursos do nltk, se ainda não estiverem instalados
nltk.download('punkt')
nltk.download('stopwords')


def processar_texto(texto):
    """Processa o texto removendo pontuação e stopwords, e retorna uma lista de palavras."""
    stop_words = set(stopwords.words('portuguese'))
    palavras = word_tokenize(texto.lower())
    palavras = [p for p in palavras if p.isalpha() and p not in stop_words]
    return palavras


def gerar_frequencia(palavras):
    """Gera um contador com a frequência das palavras."""
    return Counter(palavras)


def salvar_csv(frequencia, arquivo):
    """Salva a tabela de frequência em um arquivo CSV."""
    df = pd.DataFrame(frequencia.items(), columns=['Palavra', 'Frequência'])
    df = df.sort_values(by='Frequência', ascending=False)
    df.to_csv(arquivo, index=False)
    print(f"Tabela de frequência salva em '{arquivo}'")


def main():
    """Função principal para executar o script."""
    texto = """
    Seu texto vai aqui. Substitua este texto pelo texto que deseja analisar.
    Por exemplo, você pode usar um texto de um artigo, livro, ou qualquer outro material.
    """
    palavras = processar_texto(texto)
    frequencia = gerar_frequencia(palavras)
    salvar_csv(frequencia, 'frequencia_palavras.csv')


if __name__ == '__main__':
    main()
