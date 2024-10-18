import matplotlib.pyplot as plt
import pandas as pd

# Dados simulados de desempenho dos funcionários
dados = {
    'Data': pd.date_range(start='2023-01-01', periods=12, freq='M'),
    'Funcionário': ['Ana', 'Bob', 'Carlos', 'Diana', 'Eva', 'Felipe', 'Gina', 'Hugo', 'Iris', 'João', 'Karen', 'Lucas'],
    'Desempenho': [78, 85, 88, 90, 82, 79, 85, 87, 84, 80, 88, 91]
}

# Criar um DataFrame
df = pd.DataFrame(dados)

# Gerar gráficos
plt.figure(figsize=(12, 6))

# Gráfico de desempenho ao longo do tempo
plt.plot(df['Data'], df['Desempenho'], marker='o', linestyle='-', color='b')
plt.xlabel('Data')
plt.ylabel('Desempenho')
plt.title('Desempenho dos Funcionários ao Longo do Tempo')

# Adicionar anotações para cada ponto
for i, row in df.iterrows():
    plt.text(row['Data'], row['Desempenho'],
             f'{row["Desempenho"]}', fontsize=9, ha='right')

# Ajustar layout e salvar o gráfico
plt.tight_layout()
plt.savefig('desempenho_funcionarios.png')
plt.show()

# Gerar o relatório em formato CSV
df.to_csv('relatorio_desempenho.csv', index=False)

print("Relatório gerado com sucesso: relatorio_desempenho.csv")
print("Gráfico salvo como: desempenho_funcionarios.png")

"""
set START_DATE=2023-01-01
set DESAFIO_0=78
set DESAFIO_1=85
set DESAFIO_2=88
set DESAFIO_3=90
set DESAFIO_4=82
set DESAFIO_5=79
set DESAFIO_6=85
set DESAFIO_7=87
set DESAFIO_8=84
set DESAFIO_9=80
set DESAFIO_10=88
set DESAFIO_11=91

"""
