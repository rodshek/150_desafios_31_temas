from collections import defaultdict

import nltk
import pandas as pd
from gensim import corpora, models
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Baixar recursos do nltk, se ainda não estiverem instalados
nltk.download('punkt')
nltk.download('stopwords')


def processar_feedbacks(feedbacks):
    """Processa a lista de feedbacks removendo pontuação e stopwords, e retorna uma lista de palavras."""
    stop_words = set(stopwords.words('portuguese'))
    tokens = [word_tokenize(feedback.lower()) for feedback in feedbacks]
    tokens = [[p for p in feedback if p.isalpha() and p not in stop_words]
              for feedback in tokens]
    return tokens


def gerar_modelo_topicos(tokens):
    """Gera um modelo LDA (Latent Dirichlet Allocation) para identificar tópicos."""
    dicionario = corpora.Dictionary(tokens)
    corpus = [dicionario.doc2bow(token) for token in tokens]
    modelo = models.LdaModel(corpus, num_topics=5,
                             id2word=dicionario, passes=15)
    return modelo, dicionario


def gerar_resumo_topicos(modelo):
    """Gera um resumo dos tópicos encontrados pelo modelo LDA."""
    topicos = modelo.print_topics(num_words=5)
    resumo = []
    for i, topico in enumerate(topicos):
        resumo.append(f"Tópico {i+1}: {topico[1]}")
    return resumo


def main():
    """Função principal para executar o script."""
    feedbacks = [
        "Eu gostei muito do produto, mas o atendimento ao cliente poderia melhorar.",
        "O serviço é excelente, porém o tempo de resposta é muito longo.",
        "Muito bom, mas o preço está um pouco alto para a qualidade oferecida.",
        "Gostei do atendimento, mas o produto poderia ser mais durável.",
        "Excelente experiência, a entrega foi rápida e o produto é de alta qualidade."
    ]
    tokens = processar_feedbacks(feedbacks)
    modelo, dicionario = gerar_modelo_topicos(tokens)
    resumo = gerar_resumo_topicos(modelo)
    print("\n".join(resumo))


if __name__ == '__main__':
    main()
