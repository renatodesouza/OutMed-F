from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
import sqlite3
from flaskr.auth import login_required
from flaskr.db import get_db

lv = Blueprint('livros', __name__)


@lv.route('/lista_livro', methods=['GET'])
def lista_livro():
    con = sqlite3.connect('instance/flaskr.sqlite')
    cur = con.cursor()
    cur.execute('SELECT * FROM livro;')
    livros = cur.fetchall()
    cur.close()
    con.close()
    return render_template('blog/lista_livros.html', livros=livros)


@lv.route('/cadastrar_livro', methods=('GET', 'POST'))
def cadastrar_livro():
    if request.method == 'POST':   
        isbn = request.form['isbn']
        autor = request.form['autor']
        editora = request.form['editora']
        edicao = request.form['edicao']
        titulo = request.form['titulo']
        categoria = request.form['categoria']
        preco_compra = request.form['preco_compra']
        quantidade = request.form['quantidade']

        db = get_db()
        db.execute(
            'INSERT INTO livro (isbn, autor, editora, edicao, titulo, categoria, preco_compra, quantidade)'
            ' VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
            (isbn, autor, editora, edicao, titulo, categoria, preco_compra, quantidade)
        )
        db.commit()
        return redirect(url_for('livros.lista_livro'))
    return render_template('blog/livros.html')


@lv.route('/remover_livro/<int:isbn>', methods=['DELETE'])
def remover_livro(isbn):
    con = sqlite3.connect('instance/flaskr.sqlite')
    cur = con.cursor()
    cur.execute(f'DELETE FROM livro WHERE isbn = ?', isbn)
    return render_template('blog/livros.html')

