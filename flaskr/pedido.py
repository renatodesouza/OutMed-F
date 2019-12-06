from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
import sqlite3
from flaskr.auth import login_required
from flaskr.db import get_db

pd = Blueprint('pedido', __name__)


@pd.route('/cadastrar_pedido', methods=('GET', 'POST'))
def cadastrar_pedido():
    if request.method == 'POST':   
        isbn = request.form['isbn']
        nome_cliente = request.form['nome_cliente']
        data_pedido = request.form['data_pedido']
        valor_venda = request.form['valor_venda']
        quantidade = request.form['quantidade']
        codrastreamento = request.form['codrastreamento']

        db = get_db()
        db.execute(
            'INSERT INTO pedido (isbn, nome_cliente, data_pedido, valor_venda, quantidade, codrastreamento)'
            ' VALUES (?, ?, ?, ?, ?, ?)',
            (isbn, nome_cliente, data_pedido, valor_venda, quantidade, codrastreamento)
        )
        db.commit()
        return redirect(url_for('pedido.lista_pedido'))
    return render_template('blog/pedido.html')


@pd.route('/lista_pedido', methods=('GET', 'POST'))
def lista_pedido():
    con = sqlite3.connect('instance/flaskr.sqlite')
    cur = con.cursor()
    cur.execute('SELECT * FROM pedido;')
    pedidos = cur.fetchall()
    return render_template('blog/lista_pedido.html', pedidos=pedidos)
