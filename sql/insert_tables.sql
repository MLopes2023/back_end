use DB_MVP_SPRINT_01
;
INSERT INTO pais (id_pais, nome_pais, flag_pais_nacional, data_cadastro_pais, data_alteracao_pais) VALUES (1, 'BRASIL', 'S', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
;
INSERT INTO documento (id_documento, documento, descricao_documento, perfil_documento, data_cadastro_documento, data_alteracao_documento) VALUES (1, 'CPF', 'CADASTRO PESSOA FÍSICA', 'F', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
;
INSERT INTO documento (id_documento, documento, descricao_documento, perfil_documento, data_cadastro_documento, data_alteracao_documento) VALUES (2, 'CNPJ', 'CADASTRO PESSOA JURÍDICA', 'J', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
;
INSERT INTO classificacao (id_class, descricao_class, perfil_class, flag_nacional_class, flag_favorito_class, data_cadastro_class, data_alteracao_class )
VALUES (1, 'PESSOA FÍSICA NACIONAL', 'F', 'S', 'S', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP )
;
INSERT INTO classificacao (id_class, descricao_class, perfil_class, flag_nacional_class, flag_favorito_class, data_cadastro_class, data_alteracao_class )
VALUES (2, 'PESSOA JURÍDICA NACIONAL', 'J', 'S', 'S', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP )
;
INSERT INTO lista_restritiva
(	ident_lista,		descricao_lista,				data_cadastro_lista,		data_alteracao_lista  	)
SELECT	'LISTA-SRF',		'SRF-SECRETARIA RECEITA FEDERAL',		CURRENT_TIMESTAMP, 		CURRENT_TIMESTAMP	
UNION
SELECT	'LISTA-PEP',		'PEP-POLITICAMENTE EXPOSTO',			CURRENT_TIMESTAMP, 		CURRENT_TIMESTAMP	
UNION
SELECT	'LISTA-SPC',		'SPC-SERVIÇO DE PROTEÇÃO AO CRÉDITO',		CURRENT_TIMESTAMP, 		CURRENT_TIMESTAMP
;
INSERT INTO status_lista 
(	id_status_lista,	ident_lista_status,	codigo_status,		descricao_status,	data_cadastro_status,	 	data_alteracao_status    )
SELECT 	1,			'LISTA-SRF',		1,			'REGULAR',		CURRENT_TIMESTAMP, 		CURRENT_TIMESTAMP	 	 
UNION 
SELECT 	2,			'LISTA-SRF',		2,			'IRREGULAR',		CURRENT_TIMESTAMP, 		CURRENT_TIMESTAMP
UNION 
SELECT 	3,			'LISTA-PEP',		10,			'PEP TITULAR',		CURRENT_TIMESTAMP, 		CURRENT_TIMESTAMP
UNION
SELECT 	4,			'LISTA-PEP',		11,			'PEP RELACIONAMENTO',	CURRENT_TIMESTAMP, 		CURRENT_TIMESTAMP
UNION
SELECT 	5,			'LISTA-PEP',		12,			'RETIRADO DA LISTA',	CURRENT_TIMESTAMP, 		CURRENT_TIMESTAMP
UNION
SELECT 	6,			'LISTA-SPC',		1,			'CONSTA NA LISTA',	CURRENT_TIMESTAMP, 		CURRENT_TIMESTAMP
UNION
SELECT 	7,			'LISTA-SPC',		2,			'NADA CONSTA',		CURRENT_TIMESTAMP, 		CURRENT_TIMESTAMP
;