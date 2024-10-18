from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

# Usuários e senhas (para autenticação básica)
users = {
    "user1": "password1",
    "user2": "password2"
}


@auth.verify_password
def verify_password(username, password):
    if username in users and users[username] == password:
        return username


@app.route('/')
def home():
    return "Olá, Mundo com Autenticação!"


@app.route('/api/data', methods=['GET'])
@auth.login_required
def get_data():
    data = {
        'id': 1,
        'name': 'Exemplo Autenticado',
        'description': 'Este é um exemplo de API com autenticação.'
    }
    return jsonify(data)


@app.route('/api/greet', methods=['GET'])
@auth.login_required
def greet():
    name = request.args.get('name', 'Visitante')
    return jsonify({'message': f'Olá, {name}!'})


if __name__ == '__main__':
    app.run(debug=True)
