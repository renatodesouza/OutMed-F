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

@bp.route('/cadastrar_cliente', methods=('GET', 'POST'))
def cadastrar_cliente():
    return render_template('blog/cliente.html')

@bp.route('/lista_cliente', methods=('GET', 'POST'))
def lista_cliente():
    return render_template('blog/lista_cliente.html')

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