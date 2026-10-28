import sys
sys.path.append('./')

import pandas as pd
import src.utils.postgresql_utils as puts

#extracting data from raw tables and manipulating to put in silver tables
#insertion of silver_viagem
db_columns = [
    'id_viagem',
    'num_proposta',
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

#execute the query in chunks of 100000 lines to not overload RAM
offset = 0

while True:
    query = f'''
        SELECT {','.join(db_columns)} 
        FROM raw_viagem
        ORDER BY id_viagem
        LIMIT 100000 OFFSET {offset};
        '''
    rows = puts.execute_dql(query)

    if not rows:
        break

    #creates a dataframe from the query above
    df = pd.DataFrame(rows, columns=db_columns)

    #creates and append data from the chunk
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

#----------------
# Data convertion
#----------------

df = pd.read_csv('./data/silver/silver_viagem.csv', sep=';', encoding='latin1')

#changing Null values to NaN
df = df.replace(['NaN', 'nan', ''], float('nan'))

#duplicates
#print(df.duplicated().sum()) #99991 duplicatas
df.drop_duplicates(inplace=True)

#cargo(127931 ausentes): preencher com 'desconhecido'
df['cargo'].fillna('desconhecido', inplace=True)

#motivo(1 ausente) : substituir por 'desconhecido'
df['motivo'].fillna('desconhecido', inplace=True)

#correction of type datetime
df['data_inicio'] = pd.to_datetime(df['data_inicio'], format='%d/%m/%Y', errors='coerce')
df['data_fim'] = pd.to_datetime(df['data_fim'], format='%d/%m/%Y', errors='coerce')

#correction of type numeric
df['valor_diarias'] = pd.to_numeric(df['valor_diarias'].astype('string').str.strip().str.replace(',','.'), errors='coerce')
df['valor_passagens'] = pd.to_numeric(df['valor_passagens'].astype('string').str.strip().str.replace(',','.'), errors='coerce')
df['valor_devolucao'] = pd.to_numeric(df['valor_devolucao'].astype('string').str.strip().str.replace(',','.'), errors='coerce')
df['valor_outros'] = pd.to_numeric(df['valor_outros'].astype('string').str.strip().str.replace(',','.'), errors='coerce')

df.to_csv('./data/silver/silver_viagem.csv', sep=';', encoding='latin1', index=False)

columns = [
    'id_viagem',
    'num_proposta',
    'situacao',
    'viagem_urgente',
    'cod_orgao_superior',
    'nome_orgao_superior',
    'nome_viajante',
    'cargo',
    'data_inicio',
    'data_fim',
    'destinos',
    'motivo',
    'valor_diarias',
    'valor_passagens',
    'valor_devolucao',
    'valor_outros_gastos'
    ]

puts.batch_insert('silver_viagem', columns, './data/silver/silver_viagem.csv')
