from flask import Flask, render_template_string

app = Flask(__name__)

# Página HTML com uma mensagem personalizada
pagina_html = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mensagem Personalizada</title>
</head>
<body>
    <h1>Olá, bem-vindo ao meu aplicativo Flask!</h1>
    <p>Esta é uma mensagem personalizada exibida em uma página web.</p>
</body>
</html>
"""


@app.route('/')
def home():
    return render_template_string(pagina_html)


if __name__ == '__main__':
    app.run(debug=True)
