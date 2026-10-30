import sys
sys.path.append('./')

import src.utils.postgresql_utils as puts

#import pandas as pd
#import matplotlib.pyplot as plt

def create_gold() -> bool:
    '''
    Create the gold tables of the analysis that answers the projects questions.

    Args:
        None

    Returns:
        bool
    '''

    try:
        #--------------
        #SQL questions:
        #--------------

        #Quais os 5 orgãos com maior custo total?
        query = '''
            CREATE OR REPLACE VIEW gold_orgao_custo AS
                SELECT cod_orgao_superior, nome_orgao_superior, SUM(valor_total) AS soma
                FROM silver_viagem
                GROUP BY cod_orgao_superior, nome_orgao_superior
                ORDER BY soma DESC;
            '''

        puts.execute_ddl(query)

        #Quais os 3 destinos com maior custo médio por viagem?
        query = '''
            CREATE OR REPLACE VIEW gold_custo_viagem AS
                SELECT 
                    p.pais_destino_ida,
                    p.uf_destino_ida,
                    p.cidade_destino_ida,
                    ROUND(AVG(v.valor_total), 2) AS media_valor
                FROM silver_viagem v
                INNER JOIN silver_passagem p
                    ON v.id_viagem = p.id_viagem
                GROUP BY 
                    p.pais_destino_ida,
                    p.uf_destino_ida,
                    p.cidade_destino_ida
                ORDER BY media_valor DESC;
            '''

        puts.execute_ddl(query)

        #Qual a viagem com maior duração e seu custo total?
        query = '''
            CREATE OR REPLACE VIEW gold_maior_duracao AS
                SELECT id_viagem, valor_total, duracao_dias
                FROM silver_viagem
                ORDER BY duracao_dias DESC;
            '''

        puts.execute_ddl(query)

        #Qual o tipo de pagamento com maior valor médio?
        query = '''
            CREATE OR REPLACE VIEW gold_tipo_pagamento AS
                SELECT tipo_pagamento, AVG(valor) as valor_medio
                FROM silver_pagamento
                GROUP BY tipo_pagamento
                ORDER BY valor_medio DESC;
            '''

        puts.execute_ddl(query)

        #Qual o meio de teansporte mais usado nos trechos?
        query = '''
            CREATE OR REPLACE VIEW gold_transporte_trecho AS
                SELECT meio_transporte, COUNT(meio_transporte) AS vezes_usado
                FROM silver_trecho
                GROUP BY meio_transporte
                ORDER BY vezes_usado DESC;
            '''

        puts.execute_ddl(query)

        #Qual UF de destino mais aparece nos trechos?
        query = '''
            CREATE OR REPLACE VIEW gold_UF_trecho AS
                SELECT destino_uf, COUNT(destino_uf) AS vezes_repetido
                FROM silver_trecho
                GROUP BY destino_uf
                ORDER BY vezes_repetido DESC;
            '''

        puts.execute_ddl(query)

        #Qual orgão pagou mais no total?
        query = '''
            CREATE OR REPLACE VIEW gold_orgao_gastou AS
                SELECT nome_orgao_pagador, SUM(valor) AS soma_valor
                FROM silver_pagamento
                GROUP BY nome_orgao_pagador
                ORDER BY soma_valor DESC;
            '''

        puts.execute_ddl(query)

        return True

    except Exception as e:
        print(f'\n{e}\n')

        return False
