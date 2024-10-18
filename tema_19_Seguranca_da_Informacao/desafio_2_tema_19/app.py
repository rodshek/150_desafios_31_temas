from flask import Flask, request

app = Flask(__name__)


@app.route('/saudacao/<nome>')
def saudacao(nome):
    return f'Olá, {nome}! Bem-vindo ao meu aplicativo web!'


if __name__ == '__main__':
    app.run(debug=True)
