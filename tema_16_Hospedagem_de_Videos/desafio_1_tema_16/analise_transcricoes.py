import nltk
from gensim import corpora, models
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Baixar recursos do nltk, se ainda não estiverem instalados
nltk.download('punkt')
nltk.download('stopwords')


def processar_transcricoes(transcricoes):
    """Processa a lista de transcrições removendo pontuação e stopwords, e retorna uma lista de palavras."""
    stop_words = set(stopwords.words('portuguese'))
    tokens = [word_tokenize(transcricao.lower())
              for transcricao in transcricoes]
    tokens = [[p for p in transcricao if p.isalpha() and p not in stop_words]
              for transcricao in tokens]
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
    transcricoes = [
        "Na reunião discutimos sobre a estratégia de marketing para o próximo trimestre. A equipe sugere aumentar o orçamento.",
        "Outro ponto importante foi a necessidade de aprimorar a comunicação interna entre os departamentos.",
        "Também falamos sobre o lançamento do novo produto e como ele se alinha com os objetivos da empresa.",
        "Foi destacado que o treinamento dos funcionários é essencial para manter a qualidade do atendimento ao cliente.",
        "Por fim, discutimos a possibilidade de expandir para novos mercados internacionais."
    ]
    tokens = processar_transcricoes(transcricoes)
    modelo, dicionario = gerar_modelo_topicos(tokens)
    resumo = gerar_resumo_topicos(modelo)
    print("\n".join(resumo))


if __name__ == '__main__':
    main()
