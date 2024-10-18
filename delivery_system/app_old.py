from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restaurante.db'
db = SQLAlchemy(app)

# Models


class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente = db.Column(db.String(100), nullable=False)
    produto = db.Column(db.String(100), nullable=False)
    quantidade = db.Column(db.Integer, default=1)
    status = db.Column(db.String(100), default="Em andamento")


class Estoque(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    produto = db.Column(db.String(100), nullable=False)
    quantidade = db.Column(db.Integer, default=0)


class Caixa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente = db.Column(db.String(100), nullable=False)
    produto = db.Column(db.String(100), nullable=False)
    quantidade = db.Column(db.Integer)
    valor_total = db.Column(db.Float)
    forma_pagamento = db.Column(db.String(50))


# Criar as tabelas no banco de dados
with app.app_context():
    db.create_all()

# Rotas


@app.route('/')
def index():
    estoque_atual = Estoque.query.all()
    return render_template('index.html', estoque=estoque_atual)


@app.route('/pedido', methods=['GET', 'POST'])
def realizar_pedido():
    if request.method == 'POST':
        cliente = request.form['cliente']
        produto = request.form['produto']
        quantidade = int(request.form['quantidade'])
        novo_pedido = Pedido(
            cliente=cliente, produto=produto, quantidade=quantidade)

        # Atualiza o estoque
        item_estoque = Estoque.query.filter_by(produto=produto).first()
        if item_estoque and item_estoque.quantidade >= quantidade:
            item_estoque.quantidade -= quantidade
            db.session.add(novo_pedido)
            db.session.commit()
        else:
            return "Estoque insuficiente", 400

        return redirect(url_for('cozinha'))

    return render_template('pedido.html')


@app.route('/cozinha')
def cozinha():
    pedidos = Pedido.query.filter_by(status="Em andamento").all()
    return render_template('cozinha.html', pedidos=pedidos)


@app.route('/atualizar_pedido/<int:pedido_id>', methods=['POST'])
def atualizar_pedido(pedido_id):
    pedido = Pedido.query.get(pedido_id)
    pedido.status = "Pronto para entrega"
    db.session.commit()
    return redirect(url_for('cozinha'))


@app.route('/estoque', methods=['GET', 'POST'])
def gerenciar_estoque():
    if request.method == 'POST':
        produto = request.form['produto']
        quantidade = int(request.form['quantidade'])

        item_estoque = Estoque.query.filter_by(produto=produto).first()
        if item_estoque:
            item_estoque.quantidade += quantidade
        else:
            novo_item = Estoque(produto=produto, quantidade=quantidade)
            db.session.add(novo_item)

        db.session.commit()
        return redirect(url_for('gerenciar_estoque'))

    estoque_atual = Estoque.query.all()
    return render_template('estoque.html', estoque=estoque_atual)


@app.route('/caixa', methods=['GET', 'POST'])
def caixa():
    if request.method == 'POST':
        cliente = request.form['cliente']
        pedido = Pedido.query.filter_by(
            cliente=cliente, status="Pronto para entrega").first()

        if pedido:
            valor_total = calcular_valor_total(
                pedido.produto, pedido.quantidade)
            forma_pagamento = request.form['forma_pagamento']
            novo_caixa = Caixa(cliente=pedido.cliente, produto=pedido.produto,
                               quantidade=pedido.quantidade, valor_total=valor_total, forma_pagamento=forma_pagamento)
            db.session.add(novo_caixa)
            db.session.commit()

            # Atualiza o status do pedido para faturado
            pedido.status = "Faturado"
            db.session.commit()

        return redirect(url_for('caixa'))

    pedidos_prontos = Pedido.query.filter_by(
        status="Pronto para entrega").all()
    return render_template('caixa.html', pedidos=pedidos_prontos)


@app.route('/relatorios')
def relatorios():
    pedidos_faturados = Pedido.query.filter_by(status="Faturado").all()
    return render_template('relatorios.html', pedidos=pedidos_faturados)

# Função para calcular o valor total


def calcular_valor_total(produto, quantidade):
    precos = {"Dog": 10, "Lanche": 15, "Pizza": 8}
    return precos.get(produto, 0) * quantidade


if __name__ == '__main__':
    app.run(debug=True)
