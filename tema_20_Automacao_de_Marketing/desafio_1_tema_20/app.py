from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# Dados simulados
tasks = [
    {'id': 1, 'title': 'Learn Python', 'done': False},
    {'id': 2, 'title': 'Build an API', 'done': False}
]

class Task(Resource):
    def get(self, task_id):
        task = next((task for task in tasks if task['id'] == task_id), None)
        if task is None:
            return {'message': 'Task not found'}, 404
        return jsonify(task)

    def put(self, task_id):
        task = next((task for task in tasks if task['id'] == task_id), None)
        if task is None:
            return {'message': 'Task not found'}, 404
        
        data = request.get_json()
        task['title'] = data.get('title', task['title'])
        task['done'] = data.get('done', task['done'])
        return jsonify(task)

    def delete(self, task_id):
        global tasks
        tasks = [task for task in tasks if task['id'] != task_id]
        return {'message': 'Task deleted'}

class TaskList(Resource):
    def get(self):
        return jsonify(tasks)

    def post(self):
        data = request.get_json()
        new_task = {
            'id': len(tasks) + 1,
            'title': data['title'],
            'done': data.get('done', False)
        }
        tasks.append(new_task)
        return jsonify(new_task), 201

api.add_resource(Task, '/tasks/<int:task_id>')
api.add_resource(TaskList, '/tasks')

if __name__ == '__main__':
    app.run(debug=True)
