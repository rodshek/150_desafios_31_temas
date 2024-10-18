import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud

# Dados fictícios de um texto
texto = """
A visualização de dados é uma representação gráfica dos dados. Ela é uma ferramenta fundamental para a análise de grandes volumes de dados. A criação de gráficos, tabelas e diagramas permite que os analistas e cientistas de dados compreendam melhor as informações e compartilhem insights. A visualização de dados pode incluir gráficos de barras, gráficos de linha, mapas e muito mais. A nuvem de palavras é uma das formas mais interessantes de visualização de dados, mostrando as palavras mais frequentes em um texto.
"""

# Criar nuvem de palavras
wordcloud = WordCloud(width=800, height=400,
                      background_color='white').generate(texto)

# Criar gráfico
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')

# Adicionar título
plt.title('Nuvem de Palavras')

# Mostrar o gráfico
plt.savefig('nuvem_de_palavras.png')
plt.show()

# Exibir informações
print("A nuvem de palavras foi salva como 'nuvem_de_palavras.png'.")
