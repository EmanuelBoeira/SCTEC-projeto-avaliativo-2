import sys
sys.path.append('./')

import src.utils.postgresql_utils as puts

import pandas as pd
import matplotlib as plt

#--------------
#SQL questions:
#--------------

#quais os 5 orgãos com maior custo total?
query = '''
    SELECT cod_orgao_superior, nome_orgao_superior
    FROM silver_viagem
    ORDER BY valor_total DESC
    LIMIT 5;
    '''

result = puts.execute_dql(query)

print(result)

#quais os 3 destinos com maior custo médio por viagem?

#Qual a viagem com maior duração e seu custo total?

#---------------------
#matplotlib questions:
#---------------------

#Qual o tipo de pagamento com maior valor médio?

#Qual o meio de teansporte mais usado nos trechos?

#Qual UF de destino mais aparece nos trechos?

#Qual orgão pagou mais no total?
