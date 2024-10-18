import matplotlib.pyplot as plt
import pandas as pd

# Dados simulados de feedback de funcionários
dados = {
    'Departamento': ['Vendas', 'TI', 'RH', 'Financeiro', 'Marketing'],
    'Satisfação (0-10)': [7, 6, 8, 5, 7],
    'Áreas de Melhoria': ['Comunicação', 'Suporte', 'Benefícios', 'Gestão', 'Treinamento']
}

# Criar um DataFrame
df = pd.DataFrame(dados)

# Análise dos dados - calcular a média de satisfação
media_satisfacao = df['Satisfação (0-10)'].mean()
print(f"Média de Satisfação: {media_satisfacao:.2f}")

# Gerar gráficos
plt.figure(figsize=(10, 5))

# Gráfico de satisfação por departamento
plt.subplot(1, 2, 1)
plt.bar(df['Departamento'], df['Satisfação (0-10)'], color='skyblue')
plt.xlabel('Departamento')
plt.ylabel('Satisfação (0-10)')
plt.title('Satisfação por Departamento')

# Gráfico de áreas de melhoria
plt.subplot(1, 2, 2)
df['Áreas de Melhoria'].value_counts().plot(kind='bar', color='salmon')
plt.xlabel('Áreas de Melhoria')
plt.ylabel('Número de Feedbacks')
plt.title('Áreas de Melhoria Recomendadas')

# Ajustar layout e salvar o gráfico
plt.tight_layout()
plt.savefig('analise_feedback.png')
plt.show()

# Gerar o relatório em formato CSV
df.to_csv('relatorio_feedback.csv', index=False)

print("Relatório gerado com sucesso: relatorio_feedback.csv")
print("Gráfico salvo como: analise_feedback.png")

"""
set DEPARTAMENTO_0=Vendas
set DEPARTAMENTO_1=TI
set DEPARTAMENTO_2=RH
set DEPARTAMENTO_3=Financeiro
set DEPARTAMENTO_4=Marketing
set SATISFACAO_0=7
set SATISFACAO_1=6
set SATISFACAO_2=8
set SATISFACAO_3=5
set SATISFACAO_4=7
set AREA_MELHORIA_0=Comunicação
set AREA_MELHORIA_1=Suporte
set AREA_MELHORIA_2=Benefícios
set AREA_MELHORIA_3=Gestão
set AREA_MELHORIA_4=Treinamento

"""
