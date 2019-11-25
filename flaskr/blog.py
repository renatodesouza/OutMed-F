from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('blog', __name__)

@bp.route('/')

def index():
    # db = get_db()
    # posts = db.execute(
    #     'SELECT p.id, title, body, created, author_id, username'
    #     ' FROM post p JOIN user u ON p.author_id = u.id'
    #     ' ORDER BY created DESC'
    # ).fetchall()
    return render_template('blog/index.html')

#--------------------TEMPLATE DE TABELA BASE-------------------------
@bp.route('/tabela', methods=('GET', 'POST'))
def tabela():
    return render_template('blog/base_tabela.html')

#---------------------CLIENTE-----------------------------
@bp.route('/cadastrar_cliente', methods=('GET', 'POST'))

def cadastrar_cliente():
    return render_template('blog/cliente.html')

@bp.route('/lista_cliente', methods=('GET', 'POST'))
def lista_cliente():
    #cliente = cliente.query.all()
    return render_template('blog/lista_cliente.html')

#---------------------FORNECEDOR-----------------------------
@bp.route('/cadastrar_fornecedor', methods=('GET', 'POST'))
def cadastrar_fornecedor():
    return render_template('blog/fornecedor.html')

@bp.route('/lista_fornecedor', methods=('GET', 'POST'))
def lista_fornecedor():
    #fornecedor = fornecedor.query.all()
    return render_template('blog/lista_fornecedor.html')

#---------------------FUNCIONARIO-----------------------------
@bp.route('/cadastrar_funcionario', methods=('GET', 'POST'))
def cadastrar_funcionario():
    return render_template('blog/funcionario.html')

@bp.route('/lista_funcionario', methods=('GET', 'POST'))
def lista_funcionario():
    #devolucao = devolucao.query.all()
    return render_template('blog/lista_funcionario.html')

#---------------------PEDIDO-----------------------------
@bp.route('/cadastrar_pedido', methods=('GET', 'POST'))
def cadastrar_pedido():
    return render_template('blog/pedido.html')

@bp.route('/lista_pedido', methods=('GET', 'POST'))
def lista_pedido():
    #devolucao = devolucao.query.all()
    return render_template('blog/lista_pedido.html')

#---------------------DEVOLUCAO-----------------------------
@bp.route('/cadastrar_devolucao', methods=('GET', 'POST'))
def cadastrar_devolucao():
    return render_template('blog/devolucao.html')

@bp.route('/lista_devolucao', methods=('GET', 'POST'))
def lista_devolucao():
    #devolucao = devolucao.query.all()
    return render_template('blog/lista_devolucao.html')
    
#---------------------LIVROS-----------------------------
@bp.route('/cadastrar_livro', methods=('GET', 'POST'))
def cadastrar_livro():
    return render_template('blog/livros.html')

@bp.route('/lista_livro', methods=('GET', 'POST'))
def lista_livro():
    #livro = livro.query.all()
    return render_template('blog/lista_livros.html')



#-----------------CRIA CLIENTE----------------------------
@bp.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':   
        id = request.form['id']
        nome = request.form['nome']
        email = request.form['email']
        cidade = request.form['cidade']
        bairro = request.form['bairro']
        rua = request.form['rua']
        numero = request.form['numero']

        db = get_db()
        db.execute(
            'INSERT INTO cliente (nome, email)'
            ' VALUES (?, ?)',
            (nome, email)
        )
        db.commit()

        db.execute(
            'INSERT INTO end_cliente (id_cliente, cidade, bairro, rua, numero)'
            ' VALUES (?, ?, ?, ?, ?)',
            (id_cliente, cidade, bairro, rua, numero)
        )
        db.commit()

        return redirect(url_for('blog.lista_cliente'))

    return render_template('blog/cliente.html')