from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
import sqlite3
from flaskr.auth import login_required
from flaskr.db import get_db

fr = Blueprint('fornecedor', __name__)


@fr.route('/lista_fornecedor', methods=('GET', 'POST'))
def lista_fornecedor():
    con = sqlite3.connect('instance/flaskr.sqlite')
    cur = con.cursor()
    cur.execute('SELECT * FROM fornecedor;')
    fornecedores = cur.fetchall()
    return render_template('blog/lista_fornecedor.html', fornecedores=fornecedores)

@fr.route('/criar_fornecedor', methods=('GET', 'POST'))
def criar_fornecedor():
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

        return redirect(url_for('fornecedor.lista_fornecedor'))

    return render_template('blog/fornecedor.html')
