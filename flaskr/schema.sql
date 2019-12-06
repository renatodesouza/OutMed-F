DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS cliente;
DROP TABLE IF EXISTS funcionario;
DROP TABLE IF EXISTS fornecedor;
DROP TABLE IF EXISTS livro;
DROP TABLE IF EXISTS pedido;
DROP TABLE IF EXISTS devolucao;
DROP TABLE IF EXISTS contato_fornecedor;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  email VARCHAR (80),
  senha TEXT NOT NULL
);

CREATE TABLE cliente(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nome VARCHAR (30),
	sobrenome VARCHAR (30),
	email VARCHAR (256),
	celular VARCHAR (11),
	fone VARCHAR (11),
	cep VARCHAR (8),
	rua VARCHAR (80),
	bairro VARCHAR (10),
	cidade VARCHAR (40),
	uf VARCHAR (2),
	numero VARCHAR (10)
);

CREATE TABLE funcionario(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nome VARCHAR (80),
	email VARCHAR (80),
	celular VARCHAR (11),
	fone VARCHAR (11),
	cep VARCHAR (8),
	rua VARCHAR (80),
	bairro VARCHAR (80),
	cidade VARCHAR (80),
	uf VARCHAR (2),
	numero VARCHAR (10)
);

CREATE TABLE fornecedor(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nome VARCHAR (80),
	cnpj VARCHAR (13),
	email VARCHAR (256),
	fone1 VARCHAR (11),
	fone2 VARCHAR (11),
	cep VARCHAR (8),
	rua VARCHAR (80),
	bairro VARCHAR (80),
	cidade VARCHAR (80),
	uf VARCHAR (2),
	numero VARCHAR (10)
);

CREATE TABLE livro(
	isbn VARCHAR(13) PRIMARY KEY,
	autor VARCHAR(80),
	editora VARCHAR(40),
	edicao TINYINT,
	titulo VARCHAR (100),
	categoria VARCHAR (30),
	preco_venda DECIMAL(10, 5),
	preco_compra DECIMAL(10, 5),
	quantidade SMALLINT
);

CREATE TABLE pedido(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	isbn VARCHAR(13),
	id_cliente INTEGER,
	id_funcionario INTEGER,
	data_pedido DATE,
	valor decimal (10, 2),
	FOREIGN key (isbn) REFERENCES livro(isbn),
	FOREIGN key (id_cliente) REFERENCES cliente(id),
	FOREIGN key (id_funcionario) REFERENCES funcionario(id)
);

CREATE TABLE devolucao(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	livro VARCHAR(100),
	motivo VARCHAR(100),
	cliente VARCHAR(100)
);

CREATE TABLE contato_fornecedor(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	id_fornecedor INTEGER,
	nome VARCHAR (80),
	email VARCHAR (256),
	telefone VARCHAR(11),
	FOREIGN key (id_fornecedor) REFERENCES fornecedor(id)
);
