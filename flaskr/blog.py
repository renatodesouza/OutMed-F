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

#---------------------REPRESENTANTE-----------------------------
@bp.route('/cadastrar_representante', methods=('GET', 'POST'))
def cadastrar_representante():
    return render_template('blog/contato.html')

@bp.route('/lista_representante', methods=('GET', 'POST'))
def lista_representante():
    #devolucao = devolucao.query.all()
    return render_template('blog/listar_contato.html')

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
    
#-----------------CRIA FUNCIONARIO----------------------------
@bp.route('/create_funcionario', methods=('GET', 'POST'))
def create_funcionario():
    if request.method == 'POST':   
        id_user = request.form['id_user']
        nome = request.form['nome']
        email = request.form['email']
        celular = request.form['celular']
        fone = request.form['fone']
        cep = request.form['cep']
        rua = request.form['rua']
        bairro = request.form['bairro']
        cidade = request.form['cidade']
        uf = request.form['uf']
        numero = request.form['numero']

        db = get_db()
        db.execute(
            'INSERT INTO funcionario (id_user, nome, email, celular, fone, cep, rua, bairro, cidade, uf, numero)'
            ' VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
            (id_user, nome, email, celular, fone, cep, rua, bairro, cidade, uf, numero)
        )
        db.commit()

        return redirect(url_for('blog.index'))

    return render_template('blog/funcionario.html')

#-----------------CRIA FORNECEDOR----------------------------
@bp.route('/create_fornecedor', methods=('GET', 'POST'))
def create_fornecedor():
    if request.method == 'POST':   
        #id = request.form['id']
        nome = request.form['nome']
        cnpj = request.form['cnpj']
        email = request.form['email']
        fone1 = request.form['fone1']
        fone2 = request.form['fone2']
        cep = request.form['cep']
        rua = request.form['rua']
        bairro = request.form['bairro']
        cidade = request.form['cidade']
        uf = request.form['uf']
        numero = request.form['numero']

        db = get_db()
        db.execute(
            'INSERT INTO fornecedor (nome, cnpj, email, fone1, fone2, cep, rua, bairro, cidade, uf, numero)'
            ' VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
            (nome, cnpj, email, fone1, fone2, cep, rua, bairro, cidade, uf, numero)
        )
        db.commit()

        return redirect(url_for('blog.index'))

    return render_template('blog/fornecedor.html')


#-----------------CRIA PEDIDO----------------------------
@bp.route('/create_pedido', methods=('GET', 'POST'))
def create_pedido():
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

        return redirect(url_for('blog.index'))

    return render_template('blog/pedido.html')

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