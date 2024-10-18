import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Texto de exemplo para gerar a nuvem de palavras
texto = """
Python é uma linguagem de programação amplamente usada em diversas áreas como desenvolvimento web, ciência de dados e automação. 
A simplicidade da sintaxe e a grande quantidade de bibliotecas disponíveis fazem com que Python seja uma escolha popular entre desenvolvedores e cientistas de dados. 
Com recursos como o Pandas e o Matplotlib, Python se destaca na análise e visualização de dados.
"""

# Geração da nuvem de palavras
nuvem = WordCloud(width=800, height=400,
                  background_color='white').generate(texto)

# Exibição da nuvem de palavras
plt.figure(figsize=(10, 5))
plt.imshow(nuvem, interpolation='bilinear')
plt.axis('off')  # Remove os eixos
plt.show()
