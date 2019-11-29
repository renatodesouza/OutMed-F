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
	nome VARCHAR (80),
	sobrenome VARCHAR (130),
	email VARCHAR (80),
	celular INTEGER,
	fone INTEGER,
	cep INTEGER (10),
	rua VARCHAR (80),
	bairro VARCHAR (80),
	cidade VARCHAR (80),
	uf VARCHAR (2),
	numero VARCHAR (10)
);

CREATE TABLE funcionario(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	id_user INTEGER,
	nome VARCHAR (80),
	email VARCHAR (80),
	celular INTEGER,
	fone INTEGER,
	cep INTEGER (10),
	rua VARCHAR (80),
	bairro VARCHAR (80),
	cidade VARCHAR (80),
	uf VARCHAR (2),
	numero VARCHAR (10),
	FOREIGN KEY (id_user) REFERENCES user(id)
);

CREATE TABLE fornecedor(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nome VARCHAR (80),
	cnpj INTEGER,
	email VARCHAR (80),
	fone1 INTEGER,
	fone2 INTEGER,
	cep INTEGER,
	rua VARCHAR (80),
	bairro VARCHAR (80),
	cidade VARCHAR (80),
	uf VARCHAR (2),
	numero VARCHAR (10)
);

CREATE TABLE livro(
	isbn INTEGER PRIMARY KEY,
	autor VARCHAR(80),
	editora VARCHAR(80),
	edicao VARCHAR(50),
	titulo VARCHAR (100),
	categoria VARCHAR (80),
	preco_venda real,
	preco_compra real,
	quantidade INTEGER (100)
);

CREATE TABLE pedido(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	isbn INTEGER,
	id_cliente INTEGER,
	id_funcionario INTEGER,
	data_pedido DATE,
	valor real,
	FOREIGN key (isbn) REFERENCES livro(isbn),
	FOREIGN key (id_cliente) REFERENCES cliente(id),
	FOREIGN key (id_funcionario) REFERENCES funcionario(id)
);

CREATE TABLE devolucao(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	id_pedido INTEGER,
	id_cliente INTEGER,
	id_funcionario INTEGER,
	FOREIGN key (id_cliente) REFERENCES cliente(id)
	FOREIGN key (id_pedido) REFERENCES pedido(id)
	FOREIGN key (id_funcionario) REFERENCES funcioanrio(id)
);

CREATE TABLE contato_fornecedor(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	id_fornecedor INTEGER,
	nome VARCHAR (80),
	email VARCHAR (80),
	telefone INTEGER,
	FOREIGN key (id_fornecedor) REFERENCES fornecedor(id)
);
