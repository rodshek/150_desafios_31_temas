from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    preco = db.Column(db.Float)
    estoque = db.Column(db.Integer)


class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente = db.Column(db.String(100))
    produto = db.Column(db.String(100))
    quantidade = db.Column(db.Integer)
    # Na Cozinha, Pronto para Entrega, Entregue
    status = db.Column(db.String(50))


class Estoque(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    produto_id = db.Column(db.Integer, db.ForeignKey('produto.id'))
    quantidade = db.Column(db.Integer)


class Entregador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    status = db.Column(db.String(50))  # Disponível, Ocupado
