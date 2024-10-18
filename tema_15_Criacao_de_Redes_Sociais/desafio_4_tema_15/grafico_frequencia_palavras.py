from collections import Counter

import matplotlib.pyplot as plt
import nltk
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


def criar_grafico(frequencia, arquivo):
    """Cria um gráfico de barras e salva em um arquivo."""
    palavras, contagens = zip(*frequencia.items())
    plt.figure(figsize=(10, 6))
    plt.bar(palavras, contagens, color='skyblue')
    plt.xlabel('Palavras')
    plt.ylabel('Frequência')
    plt.title('Frequência de Palavras')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(arquivo)
    plt.show()
    print(f"Gráfico salvo em '{arquivo}'")


def main():
    """Função principal para executar o script."""
    texto = """
    Seu texto vai aqui. Substitua este texto pelo texto que deseja analisar.
    Por exemplo, você pode usar um texto de um artigo, livro, ou qualquer outro material.
    """
    palavras = processar_texto(texto)
    frequencia = gerar_frequencia(palavras)
    criar_grafico(frequencia, 'frequencia_palavras.png')


if __name__ == '__main__':
    main()
