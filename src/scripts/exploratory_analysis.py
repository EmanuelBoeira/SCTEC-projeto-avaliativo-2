import sys
sys.path.append('./')

import pandas as pd
import src.utils.postgresql_utils as puts

#extracting data from raw tables and manipulating to put in silver tables
db_columns = [
    'id_viagem',
    'situacao',
    'urgente',
    'cod_orgao_superior',
    'nome_orgao_superior',
    'nome',
    'cargo',
    'data_inicio',
    'data_fim',
    'destinos',
    'motivo',
    'valor_diarias',
    'valor_passagens',
    'valor_devolucao',
    'valor_outros'
    ]

query = f'''
    SELECT {','.join(db_columns)} FROM raw_viagem;
    '''

df = pd.DataFrame(puts.execute_dql(query), columns=db_columns)

df = df.replace(['NaN', 'nan', ''], float('nan'))
print(df.info())

#dados ausentes(341860 linhas): cargo(213929), motivo(341859)

#cargo(127931 ausentes): preencher com 'desconhecido'
df['cargo'].fillna('desconhecido', inplace=True)

#motivo(1 ausente) : remover linha ausente
df.dropna(subset='motivo', inplace=True)
print(df.info())
