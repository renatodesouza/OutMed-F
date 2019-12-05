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