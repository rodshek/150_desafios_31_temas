from flask import Flask, redirect, render_template_string, request, url_for
from flask_mail import Mail, Message

app = Flask(__name__)

# Configuração do Flask-Mail
# Substitua pelo seu servidor SMTP
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587  # Porta SMTP padrão
# Substitua pelo seu e-mail
app.config['MAIL_USERNAME'] = 'seuemail@example.com'
app.config['MAIL_PASSWORD'] = 'suasenha'  # Substitua pela sua senha
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
# Substitua pelo seu e-mail
app.config['MAIL_DEFAULT_SENDER'] = 'seuemail@example.com'

mail = Mail(app)

# Página HTML com o formulário de contato
formulario_html = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulário de Contato</title>
</head>
<body>
    <h1>Formulário de Contato</h1>
    <form method="post" action="/enviar">
        <label for="nome">Nome:</label>
        <input type="text" id="nome" name="nome" required><br>
        <label for="email">E-mail:</label>
        <input type="email" id="email" name="email" required><br>
        <label for="mensagem">Mensagem:</label><br>
        <textarea id="mensagem" name="mensagem" rows="4" cols="50" required></textarea><br>
        <input type="submit" value="Enviar">
    </form>
</body>
</html>
"""


@app.route('/')
def index():
    return render_template_string(formulario_html)


@app.route('/enviar', methods=['POST'])
def enviar():
    nome = request.form['nome']
    email = request.form['email']
    mensagem = request.form['mensagem']

    msg = Message("Novo Contato do Formulário",
                  # Substitua pelo seu e-mail
                  recipients=["seuemail@example.com"],
                  body=f"Nome: {nome}\nE-mail: {email}\nMensagem: {mensagem}")

    try:
        mail.send(msg)
        return redirect(url_for('sucesso'))
    except Exception as e:
        return str(e)


@app.route('/sucesso')
def sucesso():
    return "Mensagem enviada com sucesso!"


if __name__ == '__main__':
    app.run(debug=True)
