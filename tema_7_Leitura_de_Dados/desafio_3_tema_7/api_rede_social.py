from flask import Flask, jsonify, request

app = Flask(__name__)

# Dados fictícios de postagens
postagens = [
    {'id': 1, 'usuario': 'usuario1', 'conteudo': 'Minha primeira postagem!'},
    {'id': 2, 'usuario': 'usuario2', 'conteudo': 'Adoro Python!'}
]

# Endpoint para obter todas as postagens


@app.route('/postagens', methods=['GET'])
def obter_postagens():
    return jsonify(postagens)

# Endpoint para obter uma postagem específica


@app.route('/postagens/<int:id>', methods=['GET'])
def obter_postagem(id):
    postagem = next((p for p in postagens if p['id'] == id), None)
    if postagem is None:
        return jsonify({'erro': 'Postagem não encontrada!'}), 404
    return jsonify(postagem)

# Endpoint para criar uma nova postagem


@app.route('/postagens', methods=['POST'])
def criar_postagem():
    nova_postagem = request.get_json()
    nova_postagem['id'] = len(postagens) + 1
    postagens.append(nova_postagem)
    return jsonify(nova_postagem), 201

# Endpoint para atualizar uma postagem existente


@app.route('/postagens/<int:id>', methods=['PUT'])
def atualizar_postagem(id):
    postagem = next((p for p in postagens if p['id'] == id), None)
    if postagem is None:
        return jsonify({'erro': 'Postagem não encontrada!'}), 404
    dados = request.get_json()
    postagem.update(dados)
    return jsonify(postagem)

# Endpoint para deletar uma postagem


@app.route('/postagens/<int:id>', methods=['DELETE'])
def deletar_postagem(id):
    global postagens
    postagens = [p for p in postagens if p['id'] != id]
    return jsonify({'mensagem': 'Postagem deletada com sucesso!'})


if __name__ == '__main__':
    app.run(debug=True)
