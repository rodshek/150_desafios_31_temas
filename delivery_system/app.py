from flask import Flask, redirect, render_template, request, url_for
from models import Entregador, Estoque, Pedido, Produto, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restaurante.db'
db.init_app(app)


@app.before_first_request
def create_tables():
    db.create_all()


@app.route('/')
def index():
    produtos = Produto.query.all()
    estoque = Estoque.query.all()
    return render_template('index.html', produtos=produtos, estoque=estoque)


@app.route('/pedido', methods=['GET', 'POST'])
def pedido():
    if request.method == 'POST':
        cliente = request.form['cliente']
        produto_id = request.form['produto_id']
        quantidade = int(request.form['quantidade'])
        produto = Produto.query.get(produto_id)
        if produto:
            pedido = Pedido(cliente=cliente, produto=produto.nome,
                            quantidade=quantidade, status='Na Cozinha')
            db.session.add(pedido)
            produto.estoque -= quantidade
            db.session.commit()
            return redirect(url_for('cozinha'))
    produtos = Produto.query.all()
    return render_template('pedido.html', produtos=produtos)


@app.route('/cozinha')
def cozinha():
    pedidos = Pedido.query.filter_by(status='Na Cozinha').all()
    return render_template('cozinha.html', pedidos=pedidos)


@app.route('/estoque', methods=['GET', 'POST'])
def estoque():
    if request.method == 'POST':
        produto_id = request.form['produto_id']
        quantidade = int(request.form['quantidade'])
        produto = Produto.query.get(produto_id)
        if produto:
            produto.estoque += quantidade
            db.session.commit()
        return redirect(url_for('estoque'))
    produtos = Produto.query.all()
    return render_template('estoque.html', produtos=produtos)


@app.route('/caixa')
def caixa():
    pedidos = Pedido.query.filter_by(status='Pronto para Entrega').all()
    return render_template('caixa.html', pedidos=pedidos)


@app.route('/relatorios')
def relatorios():
    pedidos = Pedido.query.filter_by(status='Entregue').all()
    return render_template('relatorios.html', pedidos=pedidos)


@app.route('/entregador')
def entregador():
    entregadores = Entregador.query.all()
    return render_template('entregador.html', entregadores=entregadores)


if __name__ == '__main__':
    app.run(debug=True)
