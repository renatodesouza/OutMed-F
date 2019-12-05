from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
import sqlite3
from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
    return render_template('blog/index.html')


@bp.route('/cadastrar_representante', methods=('GET', 'POST'))
def cadastrar_representante():
    return render_template('blog/contato.html')

@bp.route('/lista_representante', methods=('GET', 'POST'))
def lista_representante():
    #devolucao = devolucao.query.all()
    return render_template('blog/listar_contato.html')


#---------------------DEVOLUCAO-----------------------------
@bp.route('/cadastrar_devolucao', methods=('GET', 'POST'))
def cadastrar_devolucao():
    return render_template('blog/devolucao.html')

@bp.route('/lista_devolucao', methods=('GET', 'POST'))
def lista_devolucao():
    #devolucao = devolucao.query.all()
    return render_template('blog/lista_devolucao.html')
    
    


#-----------------CRIA DEVOLUCAO----------------------------
@bp.route('/create_devolucao', methods=('GET', 'POST'))
def create_devolucao():
    if request.method == 'POST':   
        id_pedido = request.form['id_pedido']
        id_cliente = request.form['id_cliente']
        id_funcionario = request.form['id_funcionario']

        db = get_db()
        db.execute(
            'INSERT INTO devolucao (id_pedido, id_cliente, id_funcionario)'
            ' VALUES (?, ?, ?)',
            (id_pedido, id_cliente, id_funcionario)
        )
        db.commit()

        return redirect(url_for('blog.index'))

    return render_template('blog/devolucao.html')