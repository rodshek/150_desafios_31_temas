import smtplib
from email import encoders
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr

import pandas as pd

# Dados fictícios de vendas diárias
dados_vendas = {
    'Data': ['2024-07-01', '2024-07-02', '2024-07-03', '2024-07-04', '2024-07-05'],
    'Vendas': [1500, 1700, 1800, 1600, 2000],
    'Número de Clientes': [25, 30, 28, 22, 35]
}

# Criar DataFrame com os dados de vendas
vendas_df = pd.DataFrame(dados_vendas)

# Salvar DataFrame em um arquivo Excel
arquivo_excel = 'relatorio_vendas_diarias.xlsx'
vendas_df.to_excel(arquivo_excel, index=False, engine='openpyxl')

# Configuração do e-mail
email_usuario = 'seuemail@example.com'
senha_usuario = 'sua_senha'
email_destinatario = 'destinatario@example.com'
assunto = 'Relatório de Vendas Diárias'
corpo_email = 'Prezados, em anexo está o relatório de vendas diárias.'

# Criar a mensagem de e-mail
msg = MIMEMultipart()
msg['From'] = formataddr(('Seu Nome', email_usuario))
msg['To'] = email_destinatario
msg['Subject'] = assunto

# Anexar o corpo do e-mail
msg.attach(MIMEText(corpo_email, 'plain'))

# Anexar o arquivo Excel
with open(arquivo_excel, 'rb') as arquivo:
    anexo = MIMEApplication(arquivo.read(), _subtype='xlsx')
    anexo.add_header('Content-Disposition', 'attachment',
                     filename=arquivo_excel)
    msg.attach(anexo)

# Enviar o e-mail
try:
    # Substitua pelo servidor SMTP apropriado
    servidor = smtplib.SMTP('smtp.example.com', 587)
    servidor.starttls()
    servidor.login(email_usuario, senha_usuario)
    servidor.send_message(msg)
    servidor.quit()
    print(f"E-mail enviado com sucesso para {email_destinatario}.")
except Exception as e:
    print(f"Falha no envio do e-mail: {e}")
