from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
import sqlite3
from flaskr.auth import login_required
from flaskr.db import get_db

fo = Blueprint('funcionario', __name__)

@fo.route('/lista_funcionario')
def lista_funcionario():
    con = sqlite3.connect('instance/flaskr.sqlite')
    cur = con.cursor()
    cur.execute('SELECT * FROM funcionario;')
    funcionarios = cur.fetchall()
    return render_template('blog/lista_funcionario.html', funcionarios=funcionarios)


@fo.route('/cadastrar_funcionario', methods=('GET', 'POST'))
def cadastrar_funcionario():
    if request.method == 'POST':   
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
            'INSERT INTO funcionario (nome, email, celular, fone, cep, rua, bairro, cidade, uf, numero)'
            ' VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
            (nome, email, celular, fone, cep, rua, bairro, cidade, uf, numero)
        )
        db.commit()

        return redirect(url_for('funcionario.lista_funcionario'))

    return render_template('blog/funcionario.html')