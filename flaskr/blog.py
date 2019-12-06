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

@bp.route('/cadastrar_devolucao', methods=('GET', 'POST'))
def cadastrar_devolucao():
    if request.method == 'POST':   
        livro_devolvido = request.form['livro_devolvido']
        motivo = request.form['motivo']
        nome_cliente = request.form['nome_cliente']

        db = get_db()
        db.execute(
            'INSERT INTO devolucao (livro, motivo, cliente)'
            ' VALUES (?, ?, ?)',
            (livro_devolvido, motivo, nome_cliente)
        )
        db.commit()

        return redirect(url_for('blog.lista_devolucao'))

    return render_template('blog/devolucao.html')

@bp.route('/lista_devolucao', methods=('GET', 'POST'))
def lista_devolucao():
    con = sqlite3.connect('instance/flaskr.sqlite')
    cur = con.cursor()
    cur.execute('SELECT * FROM devolucao;')
    devolucoes = cur.fetchall()
    cur.close()
    con.close()
    return render_template('blog/lista_devolucao.html', devolucoes=devolucoes)