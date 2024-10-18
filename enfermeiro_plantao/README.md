# Sistema de Gerenciamento de Plantão de Enfermagem

Este é um software que simula o gerenciamento de plantões de enfermagem em um ambiente hospitalar. O sistema permite que enfermeiros façam a passagem de plantão, acessem o histórico dos pacientes, gerem relatórios em Excel, e gerenciem o estoque de medicamentos. 

## Funcionalidades Principais

- **Login do Enfermeiro**: Acesso ao sistema mediante autenticação.
- **Gestão de Plantão**: Inserção e monitoramento de pacientes e tarefas.
- **Histórico de Pacientes**: Visualização do histórico de atendimento de cada paciente.
- **Relatórios em Excel**: Geração de relatórios de pacientes e plantões no formato Excel.
- **Controle de Medicamentos e Estoque**: Monitoramento do estoque de medicamentos.
  
## Estrutura do Projeto

```bash
enfermeiro_plantao/
│
├── assets/                    # Arquivos de recursos como ícones e imagens
│   └── logo.png
│
├── src/                       # Diretório principal de código-fonte
│   ├── __init__.py            # Indica que é um pacote Python
│   ├── main.py                # Arquivo principal que executa o programa
│   ├── gui/                   # Módulo de interface gráfica
│   │   ├── __init__.py
│   │   ├── login_gui.py       # Tela de login
│   │   ├── main_gui.py        # Tela principal do sistema
│   │   ├── plantao_gui.py     # Tela para plantão de enfermagem
│   │   ├── historico_gui.py   # Tela para visualizar histórico de pacientes
│   │   └── relatorios_gui.py  # Tela para gerar relatórios
│   ├── models/                # Módulo de lógica de negócios
│   │   ├── __init__.py
│   │   ├── enfermeiro.py      # Classe e lógica para os enfermeiros
│   │   ├── paciente.py        # Classe para representar os pacientes
│   │   └── plantao.py         # Classe para o plantão
│   ├── services/              # Módulo de serviços auxiliares
│   │   ├── __init__.py
│   │   ├── database.py        # Simulação de banco de dados
│   │   ├── excel_exporter.py  # Função para exportar relatórios em Excel
│   │   ├── estoque.py         # Função para gerenciar estoque de medicamentos
│   │   └── utils.py           # Funções utilitárias gerais
│
├── requirements.txt           # Lista de dependências e bibliotecas
└── README.md                  # Documentação do projeto
