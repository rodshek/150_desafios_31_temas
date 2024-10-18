from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)
auth = HTTPBasicAuth()

# Usuários e Tarefas em memória (para simplicidade)
users = {"user": "password"}
tasks = []

# Função de verificação de senha


@auth.verify_password
def verify_password(username, password):
    if username in users and users[username] == password:
        return username

# Classe para a tarefa


class Task(Resource):
    def get(self, task_id):
        if 0 <= task_id < len(tasks):
            return jsonify(tasks[task_id])
        return {'message': 'Task not found'}, 404

    @auth.login_required
    def post(self, task_id):
        if 0 <= task_id < len(tasks):
            return {'message': 'Task ID already exists'}, 400
        task = request.json
        tasks.append(task)
        return jsonify(task), 201

    @auth.login_required
    def put(self, task_id):
        if 0 <= task_id < len(tasks):
            tasks[task_id] = request.json
            return jsonify(tasks[task_id])
        return {'message': 'Task not found'}, 404

    @auth.login_required
    def delete(self, task_id):
        if 0 <= task_id < len(tasks):
            task = tasks.pop(task_id)
            return jsonify(task)
        return {'message': 'Task not found'}, 404

# Rota para a lista de tarefas


class TaskList(Resource):
    @auth.login_required
    def get(self):
        return jsonify(tasks)


# Adiciona as rotas da API
api.add_resource(Task, '/tasks/<int:task_id>')
api.add_resource(TaskList, '/tasks')

if __name__ == '__main__':
    app.run(debug=True)
