from flask import Flask, jsonify, request
from flask_jwt_extended import (JWTManager, create_access_token,
                                get_jwt_identity, jwt_required)

app = Flask(__name__)

# Configurações do JWT
# Mude isso para uma chave secreta forte
app.config['JWT_SECRET_KEY'] = 'supersecretkey'
jwt = JWTManager(app)

# Dados fictícios de usuários
usuarios = {
    'usuario1': 'senha1',
    'usuario2': 'senha2'
}

# Endpoint para login e geração de token


@app.route('/login', methods=['POST'])
def login():
    dados = request.get_json()
    usuario = dados.get('usuario')
    senha = dados.get('senha')

    if usuario not in usuarios or usuarios[usuario] != senha:
        return jsonify({'erro': 'Usuário ou senha inválidos!'}), 401

    access_token = create_access_token(identity=usuario)
    return jsonify(access_token=access_token)

# Endpoint protegido que requer autenticação


@app.route('/protegido', methods=['GET'])
@jwt_required()
def protegido():
    usuario = get_jwt_identity()
    return jsonify({'mensagem': f'Olá, {usuario}!'})


if __name__ == '__main__':
    app.run(debug=True)
