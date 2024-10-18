from flask import Flask, jsonify, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configurações do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mensagens.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa o banco de dados e o migrador
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Modelo de dados para Usuário e Mensagem


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    mensagens_enviadas = db.relationship(
        'Mensagem', backref='remetente', lazy=True)


class Mensagem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.String(255), nullable=False)
    remetente_id = db.Column(
        db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    destinatario_username = db.Column(db.String(80), nullable=False)

# Endpoint para criar um novo usuário


@app.route('/usuario', methods=['POST'])
def criar_usuario():
    dados = request.get_json()
    username = dados.get('username')
    if Usuario.query.filter_by(username=username).first():
        return jsonify({'erro': 'Usuário já existe!'}), 400
    usuario = Usuario(username=username)
    db.session.add(usuario)
    db.session.commit()
    return jsonify({'mensagem': 'Usuário criado com sucesso!'})

# Endpoint para enviar uma mensagem


@app.route('/mensagem', methods=['POST'])
def enviar_mensagem():
    dados = request.get_json()
    remetente_username = dados.get('remetente')
    destinatario_username = dados.get('destinatario')
    texto = dados.get('texto')

    remetente = Usuario.query.filter_by(username=remetente_username).first()
    destinatario = Usuario.query.filter_by(
        username=destinatario_username).first()

    if not remetente or not destinatario:
        return jsonify({'erro': 'Usuário remetente ou destinatário não encontrado!'}), 404

    mensagem = Mensagem(texto=texto, remetente=remetente,
                        destinatario_username=destinatario_username)
    db.session.add(mensagem)
    db.session.commit()
    return jsonify({'mensagem': 'Mensagem enviada com sucesso!'})

# Endpoint para listar mensagens recebidas por um usuário


@app.route('/mensagens/<string:username>', methods=['GET'])
def listar_mensagens(username):
    usuario = Usuario.query.filter_by(username=username).first()
    if not usuario:
        return jsonify({'erro': 'Usuário não encontrado!'}), 404
    mensagens = Mensagem.query.filter_by(destinatario_username=username).all()
    mensagens_list = [{'id': msg.id, 'texto': msg.texto,
                       'remetente': msg.remetente.username} for msg in mensagens]
    return jsonify(mensagens_list)


if __name__ == '__main__':
    app.run(debug=True)
