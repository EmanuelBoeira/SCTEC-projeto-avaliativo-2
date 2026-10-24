import sys
sys.path.append('./')

import pandas as pd
import src.utils.postgresql_utils as puts

#extracting data from raw tables and manipulating to put in silver tables
#insertion of silver_viagem
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

offset = 0

while True:
    query = f'''
        SELECT {','.join(db_columns)} FROM raw_viagem
        LIMIT 100000 OFFSET {offset};
        '''
    rows = puts.execute_dql(query)

    if not rows:
        break

    #creates a dataframe from the query above
    df = pd.DataFrame(rows, columns=db_columns)


    df.to_csv(
        './data/silver/silver_viagem.csv',
        mode='w' if offset == 0 else 'a',
        sep=';',
        encoding='latin1',
        index=False,
        header= True if offset == 0 else False
    )

    offset += 100000

    print('lote gravado!')
    
    del df, rows

#---------------
#data converting
#---------------

df = pd.read_csv('./data/silver/silver_viagem.csv', sep=';', encoding='latin1')

#changing Null values to NaN
df = df.replace(['NaN', 'nan', ''], float('nan'))

#cargo(127931 ausentes): preencher com 'desconhecido'
df['cargo'].fillna('desconhecido', inplace=True)

#motivo(1 ausente) : remover linha ausente
df.dropna(subset='motivo', inplace=True)

#correction of type datetime
df['data_inicio'] = pd.to_datetime(df['data_inicio'], format='%d/%m/%Y', errors='coerce')
df['data_fim'] = pd.to_datetime(df['data_fim'], format='%d/%m/%Y', errors='coerce')

#correction of type numeric
df ['valor_diarias'] = df['valor_diarias'].str.strip().str.replace(',', '.')
df ['valor_passagens'] = df['valor_passagens'].str.strip().str.replace(',', '.')
df ['valor_devolucao'] = df['valor_devolucao'].str.strip().str.replace(',', '.')
df ['valor_outros'] = df['valor_outros'].str.strip().str.replace(',', '.')
    
df['valor_diarias'] = pd.to_numeric(df['valor_diarias'], errors='coerce')
df['valor_passagens'] = pd.to_numeric(df['valor_passagens'], errors='coerce')
df['valor_devolucao'] = pd.to_numeric(df['valor_devolucao'], errors='coerce')
df['valor_outros'] = pd.to_numeric(df['valor_outros'], errors='coerce')

df.to_csv('./data/silver/silver_viagem.csv', sep=';', encoding='latin1', index=False)
