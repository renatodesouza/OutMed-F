from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_pyfile('config.py')
database = SQLAlchemy(app)


@app.route('/hello')
def hello():
    return 'Hello, World!'

from . import db
db.init_app(app)

#Registrando o Blueprint de autenticação
from . import auth
app.register_blueprint(auth.bp)

#Registrando o Blueprint do blog
from . import blog
app.register_blueprint(blog.bp)
app.add_url_rule('/', endpoint='index')
