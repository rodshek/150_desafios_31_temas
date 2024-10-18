from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# Inicializar o aplicativo Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./voting.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar o banco de dados
db = SQLAlchemy(app)

# Definir o modelo para a tabela de candidatos e votos


class Candidate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    votes = db.Column(db.Integer, default=0)


# Criar as tabelas
with app.app_context():
    db.create_all()

# Rota para adicionar um novo candidato


@app.route('/add_candidate', methods=['POST'])
def add_candidate():
    data = request.json
    name = data.get('name')
    if not name:
        return jsonify({'message': 'Candidate name is required'}), 400

    candidate = Candidate(name=name)
    db.session.add(candidate)
    db.session.commit()
    return jsonify({'message': f'Candidate {name} added'}), 201

# Rota para votar em um candidato


@app.route('/vote', methods=['POST'])
def vote():
    data = request.json
    candidate_id = data.get('candidate_id')
    if not candidate_id:
        return jsonify({'message': 'Candidate ID is required'}), 400

    candidate = Candidate.query.get(candidate_id)
    if not candidate:
        return jsonify({'message': 'Candidate not found'}), 404

    candidate.votes += 1
    db.session.commit()
    return jsonify({'message': f'Voted for {candidate.name}'}), 200

# Rota para obter todos os candidatos e seus votos


@app.route('/candidates', methods=['GET'])
def get_candidates():
    candidates = Candidate.query.all()
    return jsonify([
        {'id': candidate.id, 'name': candidate.name, 'votes': candidate.votes}
        for candidate in candidates
    ]), 200


# Rodar o aplicativo
if __name__ == '__main__':
    app.run(debug=True)
