from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('blog', __name__)

@bp.route('/')

def index():
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
    
#---------------------LIVROS-----------------------------
@bp.route('/cadastrar_livro', methods=('GET', 'POST'))
def cadastrar_livro():
    return render_template('blog/livros.html')

@bp.route('/lista_livro', methods=('GET', 'POST'))
def lista_livro():
    
    return render_template('blog/lista_livros.html')

#-----------------CRIA CLIENTE----------------------------
@bp.route('/create_cliente', methods=('GET', 'POST'))
def create_cliente():
    if request.method == 'POST':   
        #id = request.form['id']
        nome = request.form['nome']
        sobrenome = request.form['sobrenome']
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
            'INSERT INTO cliente (nome, sobrenome, email, celular, fone, cep, rua, bairro, cidade, uf, numero)'
            ' VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
            (nome, sobrenome, email, celular, fone, cep, rua, bairro, cidade, uf, numero)
        )
        db.commit()

        return redirect(url_for('blog.index'))

    return render_template('blog/cliente.html')

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

#-----------------CRIA LIVRO----------------------------
@bp.route('/create_livro', methods=('GET', 'POST'))
def create_livro():
    if request.method == 'POST':   
        isbn = request.form['isbn']
        autor = request.form['autor']
        editora = request.form['editora']
        edicao = request.form['edicao']
        titulo = request.form['titulo']
        categoria = request.form['categoria']
        preco_venda = request.form['preco_venda']
        preco_compra = request.form['preco_compra']
        quantidade = request.form['quantidade']

        db = get_db()
        db.execute(
            'INSERT INTO livro (isbn, autor, editora, edicao, titulo, categoria, preco_venda, preco_compra, quantidade)'
            ' VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
            (isbn, autor, editora, edicao, titulo, categoria, preco_venda, preco_compra, quantidade)
        )
        db.commit()

        return redirect(url_for('blog.index'))

    return render_template('blog/livros.html')

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