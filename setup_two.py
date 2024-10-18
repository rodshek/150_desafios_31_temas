import os

# Lista dos temas com os títulos
temas = [
    "tema_1_Desenvolvimento_Humano",
    "tema_2_Data_Science",
    "tema_3_Machine_Learning",
    "tema_4_Visualizacao_de_Dados_e_Analise_de_Dados",
    "tema_5_Desenvolvimento_Web",
    "tema_6_Automacao_de_Scripts",
    "tema_7_Leitura_de_Dados",
    "tema_8_Escrita_de_Dados",
    "tema_9_Automacao_Comercial_em_Restaurantes",
    "tema_10_E_commerce",
    "tema_11_Automacao_Comercial_para_Lojas_de_Moveis",
    "tema_12_Automacao_Comercial_em_Mercados_Pequenos",
    "tema_13_Automacao_Comercial_em_Loja_de_Roupas",
    "tema_14_Rede_Social",
    "tema_15_Criacao_de_Redes_Sociais",
    "tema_16_Hospedagem_de_Videos",
    "tema_17_Desenvolvimento_Sustentavel",
    "tema_18_Educacao_e_Treinamento_Online",
    "tema_19_Seguranca_da_Informacao",
    "tema_20_Automacao_de_Marketing",
    "tema_21_Analise_de_Big_Data",
    "tema_22_Realidade_Aumentada_e_Realidade_Virtual",
    "tema_23_Computacao_em_Nuvem",
    "tema_24_Internet_das_Coisas_IoT",
    "tema_25_Desenvolvimento_de_APIs_em_Python",
    "tema_26_Testes_e_Debugging_em_Python",
    "tema_27_Programacao_Paralela_e_Concorrente_em_Python",
    "tema_28_Implementacao_de_Algoritmos_de_Machine_Learning_em_Python",
    "tema_29_Processamento_de_Dados_e_Analise_com_Python",
    "tema_30_Automatizacao_de_Tarefas_e_Web_Scraping_em_Python",
    "tema_31_Desenvolvimento_de_Jogos_e_Simulacoes_em_Python"
]

# Criação das pastas
for tema in temas:
    os.makedirs(tema, exist_ok=True)
