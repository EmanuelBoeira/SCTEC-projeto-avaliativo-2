--Tabelas raw(dados brutos do csv)

DROP TABLE IF EXISTS raw_viagem CASCADE;
DROP TABLE IF EXISTS raw_trecho CASCADE;
DROP TABLE IF EXISTS raw_passagem CASCADE;
DROP TABLE IF EXISTS raw_pagamento CASCADE;

CREATE TABLE raw_viagem(
	id_viagem VARCHAR(20),
	num_proposta VARCHAR(20),
	situacao VARCHAR(50),
	urgente VARCHAR(20),
	justificativa_urgente VARCHAR(2000),
	cod_orgao_superior VARCHAR(20),
	nome_orgao_superior VARCHAR(255),
	cod_orgao_solicitante VARCHAR(20),
	nome_orgao_solicitante VARCHAR(255),
	cpf VARCHAR(15),
	nome VARCHAR(255),
	cargo VARCHAR(255),
	funcao VARCHAR(255),
	descricao_funcao VARCHAR(255),
	data_inicio VARCHAR(30),
	data_fim VARCHAR(30),
	destinos VARCHAR(2000),
	motivo VARCHAR(2000),
	valor_diarias VARCHAR(10),
	valor_passagens VARCHAR(10),
	valor_devolucao VARCHAR(10),
	valor_outros VARCHAR(10)
);

CREATE TABLE raw_trecho(
	id_viagem VARCHAR(20),
	num_proposta VARCHAR(20),
	sequencia_trecho VARCHAR(20),
	origem_data VARCHAR(30),
	origem_pais VARCHAR(60),
	origem_uf VARCHAR(40),
	origem_cidade VARCHAR(80),
	destino_data VARCHAR(30),
	destino_pais VARCHAR(60),
	destino_uf VARCHAR(40),
	destino_cidade VARCHAR(80),
	meio_transp VARCHAR(50),
	num_diarias VARCHAR(10),
	missao VARCHAR(100)
);

CREATE TABLE raw_passagem(
	id_viagem VARCHAR(20),
	num_proposta VARCHAR(20),
	meio_transp VARCHAR(50),
	origem_ida_pais VARCHAR(60),
	origem_ida_uf VARCHAR(40),
	origem_ida_cidade VARCHAR(80),
	destino_ida_pais VARCHAR(60),
	destino_ida_uf VARCHAR(40),
	destino_ida_cidade VARCHAR(80),
	origem_volta_pais VARCHAR(60),
	origem_volta_uf VARCHAR(40),
	origem_volta_cidade VARCHAR(80),
	destino_volta_pais VARCHAR(60),
	destino_volta_uf VARCHAR(40),
	destino_volta_cidade VARCHAR(80),
	valor_passagem VARCHAR(20),
	taxa_servico VARCHAR(20),
	data_compra VARCHAR(15),
	hora_compra VARCHAR(20)
);

CREATE TABLE raw_pagamento(
	id_viagem VARCHAR(20),
	num_proposta VARCHAR(20),
	cod_orgao_superior VARCHAR(20),
	nome_orgao_superior VARCHAR(255),
	cod_orgao_pagador VARCHAR(20),
	nome_orgao_pagador VARCHAR(255),
	cod_un_gestora_pagadora VARCHAR(20),
	nome_un_gestora_pagadora VARCHAR(255),
	tipo_pagamento VARCHAR(50),
	valor VARCHAR(20)
);

--Tabelas silver(dados com tratamentos de tipo valores nulos)

DROP TABLE IF EXISTS silver_viagem CASCADE;
DROP TABLE IF EXISTS silver_trecho CASCADE;
DROP TABLE IF EXISTS silver_passagem CASCADE;
DROP TABLE IF EXISTS silver_pagamento CASCADE;

CREATE TABLE silver_viagem(
	id_viagem VARCHAR(20) PRIMARY KEY,
	num_proposta VARCHAR(20),
	situacao VARCHAR(50),
	viagem_urgente VARCHAR(5),
	cod_orgao_superior VARCHAR(20),
	nome_orgao_superior VARCHAR(255) NOT NULL,
	nome_viajante VARCHAR(255),
	cargo VARCHAR(255),
	data_inicio DATE,
	data_fim DATE,
	destinos VARCHAR(4000),
	motivo VARCHAR(4000),
	valor_diarias DECIMAL(10,2) CHECK (valor_diarias >= 0),
	valor_passagens DECIMAL(10,2),
	valor_devolucao DECIMAL(10,2),
	valor_outros_gastos DECIMAL(10,2),
	valor_total DECIMAL(12,2)
		GENERATED ALWAYS AS (
			COALESCE(valor_diarias, 0) + 
			COALESCE(valor_passagens, 0) + 
			COALESCE(valor_devolucao, 0) + 
			COALESCE(valor_outros_gastos, 0)
			) STORED,
	duracao_dias INT
		GENERATED ALWAYS AS (data_fim - data_inicio) STORED
);

CREATE TABLE silver_passagem(
	id_passagem SERIAL PRIMARY KEY,
	id_viagem VARCHAR(20) REFERENCES silver_viagem(id_viagem),
	meio_transporte VARCHAR(50),
	pais_origem_ida VARCHAR(60),
	uf_origem_ida VARCHAR(40),
	cidade_origem_ida VARCHAR(80),
	pais_destino_ida VARCHAR(60),
	uf_destino_ida VARCHAR(40),
	cidade_destino_ida VARCHAR(80),
	valor_passagem DECIMAL(10,2) CHECK (valor_passagem >= 0),
	taxa_servico DECIMAL(10,2) CHECK (taxa_servico >= 0),
	data_emissao DATE
);

CREATE TABLE silver_pagamento(
	id_pagamento SERIAL PRIMARY KEY,
	id_viagem VARCHAR(20) REFERENCES silver_viagem(id_viagem) NOT NULL,
	num_proposta  VARCHAR(20),
	nome_orgao_pagador VARCHAR(255),
	nome_ug_pagadora VARCHAR(255),
	tipo_pagamento VARCHAR(50) NOT NULL,
	valor DECIMAL(10,2) CHECK (valor >= 0)
);

CREATE TABLE silver_trecho(
	id_trecho SERIAL PRIMARY KEY,
	id_viagem VARCHAR(20) REFERENCES silver_viagem(id_viagem) NOT NULL,
	sequencia_trecho INT UNIQUE,
	origem_data DATE,
	origem_uf VARCHAR(40),
	origem_cidade VARCHAR(80),
	destino_data DATE,
	destino_uf VARCHAR(40),
	destino_cidade VARCHAR(80),
	meio_transporte VARCHAR(50),
	numero_diarias DECIMAL(10,2) CHECK (numero_diarias >= 0)
);
