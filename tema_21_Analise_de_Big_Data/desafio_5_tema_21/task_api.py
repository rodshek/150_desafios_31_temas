from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy

# Inicializar o aplicativo Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/task_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar o banco de dados
db = SQLAlchemy(app)
api = Api(app)

# Definir o modelo para a tabela de tarefas


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    done = db.Column(db.Boolean, default=False)


# Criar as tabelas
with app.app_context():
    db.create_all()

# Recurso para gerenciar tarefas


class TaskResource(Resource):
    def get(self, task_id):
        task = Task.query.get(task_id)
        if not task:
            return {'message': 'Task not found'}, 404
        return {
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'done': task.done
        }

    def put(self, task_id):
        data = request.json
        task = Task.query.get(task_id)
        if not task:
            return {'message': 'Task not found'}, 404

        task.title = data.get('title', task.title)
        task.description = data.get('description', task.description)
        task.done = data.get('done', task.done)
        db.session.commit()
        return {'message': 'Task updated'}

    def delete(self, task_id):
        task = Task.query.get(task_id)
        if not task:
            return {'message': 'Task not found'}, 404

        db.session.delete(task)
        db.session.commit()
        return {'message': 'Task deleted'}

# Recurso para listar e criar tarefas


class TaskListResource(Resource):
    def get(self):
        tasks = Task.query.all()
        return [{
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'done': task.done
        } for task in tasks]

    def post(self):
        data = request.json
        new_task = Task(
            title=data['title'],
            description=data.get('description'),
            done=data.get('done', False)
        )
        db.session.add(new_task)
        db.session.commit()
        return {'message': 'Task created', 'id': new_task.id}, 201


# Adicionar recursos à API
api.add_resource(TaskListResource, '/tasks')
api.add_resource(TaskResource, '/tasks/<int:task_id>')

# Rodar o aplicativo
if __name__ == '__main__':
    app.run(debug=True)
