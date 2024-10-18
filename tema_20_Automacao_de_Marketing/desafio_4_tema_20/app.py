from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flask_security import (RoleMixin, Security, SQLAlchemyUserDatastore,
                            UserMixin, login_required)
from flask_security.utils import hash_password
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///security.db'
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['SECURITY_REGISTERABLE'] = True
app.config['SECURITY_PASSWORD_SALT'] = 'salty'
db = SQLAlchemy(app)
api = Api(app)

# Define models
roles_users = db.Table('roles_users',
                       db.Column('user_id', db.Integer(),
                                 db.ForeignKey('user.id')),
                       db.Column('role_id', db.Integer(),
                                 db.ForeignKey('role.id'))
                       )


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))


# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

# Initialize database


@app.before_first_request
def create_tables():
    db.create_all()
    if not User.query.filter_by(email='admin@example.com').first():
        user_datastore.create_user(
            email='admin@example.com', password=hash_password('password'))
        db.session.commit()

# Define API Resources


class HelloWorld(Resource):
    @login_required
    def get(self):
        return {'message': 'Hello, World!'}


api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
