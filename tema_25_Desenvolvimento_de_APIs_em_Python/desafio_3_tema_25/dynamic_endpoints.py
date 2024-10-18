from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def home():
    return "Olá, Mundo com Endpoints Dinâmicos!"


@app.route('/api/hello/<string:name>', methods=['GET'])
def hello(name):
    return jsonify({'message': f'Olá, {name}!'})


@app.route('/api/square/<int:number>', methods=['GET'])
def square(number):
    return jsonify({'number': number, 'square': number ** 2})


@app.route('/api/echo', methods=['POST'])
def echo():
    data = request.json
    return jsonify({'received': data})


if __name__ == '__main__':
    app.run(debug=True)
