DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS cliente;
DROP TABLE IF EXISTS funcioanrio;
DROP TABLE IF EXISTS fornecedor;
DROP TABLE IF EXISTS livro;
DROP TABLE IF EXISTS pedido;
DROP TABLE IF EXISTS end_cliente;
DROP TABLE IF EXISTS end_fornecedor;
DROP TABLE IF EXISTS end_funcionario;
DROP TABLE IF EXISTS fone_cliente;
DROP TABLE IF EXISTS fone_fornecedor;
DROP TABLE IF EXISTS fone_funcionario;
DROP TABLE IF EXISTS contato_fornecedor;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  senha TEXT NOT NULL
);

CREATE TABLE cliente(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nome VARCHAR (80),
	email VARCHAR (80)
);

CREATE TABLE funcionario(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_user INTEGER,
  	nome VARCHAR (80),
  	email VARCHAR (80),
    cpf VARCHAR (80),
    FOREIGN KEY (id_user) REFERENCES user(id)
);

CREATE TABLE fornecedor(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
  	nome VARCHAR (80),
  	email VARCHAR (80),
    cnpj VARCHAR (100)
);

CREATE TABLE livro(
	isbn INTEGER PRIMARY KEY,
  	autor VARCHAR(80),
  	editora VARCHAR(80),
  	edicao VARCHAR(50),
  	titulo VARCHAR (100),
  	categoria VARCHAR (80)
);

CREATE TABLE pedido(
	id INTEGER PRIMARY KEY,
  	isbn INTEGER,
  	id_cliente INTEGER,
  	id_funcionario INTEGER,
  	data_pedido DATE,
  	valor real,
  	FOREIGN key (isbn) REFERENCES livro(isbn)
);

CREATE TABLE end_cliente(
	id INTEGER PRIMARY KEY,
  	id_cliente INTEGER,
  	cidade VARCHAR (80),
  	bairro VARCHAR (80),
  	rua VARCHAR (80),
  	numero VARCHAR (10),
  	FOREIGN key (id_cliente) REFERENCES cliente(id)
);

CREATE TABLE end_fornecedor(
	id INTEGER PRIMARY KEY,
  	id_fornecedor INTEGER,
  	cidade VARCHAR (80),
  	bairro VARCHAR (80),
  	rua VARCHAR (80),
  	numero VARCHAR (10),
  	FOREIGN key (id_fornecedor) REFERENCES fornecedor(id)
);

CREATE TABLE end_funcionario(
	id INTEGER PRIMARY KEY,
  	id_funcionario INTEGER,
  	cidade VARCHAR (80),
  	bairro VARCHAR (80),
  	rua VARCHAR (80),
  	numero VARCHAR (10),
  	FOREIGN key (id_funcionario) REFERENCES funcionario(id)
);

CREATE TABLE fone_funcionario(
	id INTEGER PRIMARY KEY,
  	id_funcionario INTEGER,
  	fone1 INTEGER,
  	fone2 INTEGER,
  	FOREIGN key (id_funcionario) REFERENCES funcionario(id)
);

CREATE TABLE fone_fornecedor(
	id INTEGER PRIMARY KEY,
  	id_fornecedor INTEGER,
  	fone1 INTEGER,
  	fone2 INTEGER,
  	FOREIGN key (id_fornecedor) REFERENCES fornecedor(id)
);


CREATE TABLE contato_fornecedor(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
  	id_fornecedor INTEGER,
  	nome VARCHAR (80),
  	email VARCHAR (80),
  	FOREIGN key (id_fornecedor) REFERENCES fornecedor(id)
);