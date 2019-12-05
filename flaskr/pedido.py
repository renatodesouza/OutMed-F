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
        #id = request.form['id']
        isbn = request.form['isbn']
        id_cliente = request.form['id_cliente']
        id_funcionario = request.form['id_funcionario']
        data_pedido = request.form['data_pedido']
        valor = request.form['valor']

        db = get_db()
        db.execute(
            'INSERT INTO pedido (isbn, id_cliente, id_funcionario, data_pedido, valor)'
            ' VALUES (?, ?, ?, ?, ?)',
            (isbn, id_cliente, id_funcionario, data_pedido, valor)
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
