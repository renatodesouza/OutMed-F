from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
import sqlite3
from flaskr.auth import login_required
from flaskr.db import get_db


cl = Blueprint('clientes', __name__)


@cl.route('/lista_cliente', methods=('GET', 'POST'))
def lista_cliente():
    con = sqlite3.connect('instance/flaskr.sqlite')
    cur = con.cursor()
    cur.execute('SELECT * FROM cliente;')
    clientes = cur.fetchall()
    return render_template('blog/lista_cliente.html', clientes=clientes)


@cl.route('/cadastrar_cliente', methods=('GET', 'POST'))
def cadastrar_cliente():
    if request.method == 'POST':   
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

        return redirect(url_for('clientes.lista_cliente'))

    return render_template('blog/cliente.html')
    