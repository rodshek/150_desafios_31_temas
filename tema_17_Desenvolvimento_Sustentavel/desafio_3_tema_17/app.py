from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# Lista para armazenar as tarefas (em memória)
tarefas = []


class Tarefa(Resource):
    def get(self, tarefa_id):
        for tarefa in tarefas:
            if tarefa['id'] == tarefa_id:
                return jsonify(tarefa)
        return {'message': 'Tarefa não encontrada'}, 404

    def put(self, tarefa_id):
        data = request.get_json()
        for tarefa in tarefas:
            if tarefa['id'] == tarefa_id:
                tarefa.update(data)
                return jsonify(tarefa)
        return {'message': 'Tarefa não encontrada'}, 404

    def delete(self, tarefa_id):
        global tarefas
        tarefas = [tarefa for tarefa in tarefas if tarefa['id'] != tarefa_id]
        return {'message': 'Tarefa excluída'}


class Tarefas(Resource):
    def get(self):
        return jsonify(tarefas)

    def post(self):
        data = request.get_json()
        if 'id' not in data or 'titulo' not in data or 'descricao' not in data:
            return {'message': 'Dados inválidos'}, 400
        tarefas.append(data)
        return jsonify(data), 201


api.add_resource(Tarefas, '/tarefas')
api.add_resource(Tarefa, '/tarefas/<int:tarefa_id>')

if __name__ == '__main__':
    app.run(debug=True)
