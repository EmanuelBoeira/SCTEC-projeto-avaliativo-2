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
		GENERATED ALWAYS AS (valor_diarias + valor_passagens + valor_devolucao + valor_outros_gastos) STORED,
	duracao_dias INT
		GENERATED ALWAYS AS (data_fim - data_inicio) STORED
);
