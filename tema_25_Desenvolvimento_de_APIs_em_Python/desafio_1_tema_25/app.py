from flask import Flask, jsonify, request

app = Flask(__name__)

# Definindo uma rota simples


@app.route('/')
def home():
    return "Olá, Mundo!"

# Definindo uma rota que retorna dados em formato JSON


@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        'id': 1,
        'name': 'Exemplo',
        'description': 'Este é um exemplo de API.'
    }
    return jsonify(data)

# Definindo uma rota que aceita parâmetros e retorna dados


@app.route('/api/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'Visitante')
    return jsonify({'message': f'Olá, {name}!'})


if __name__ == '__main__':
    app.run(debug=True)
