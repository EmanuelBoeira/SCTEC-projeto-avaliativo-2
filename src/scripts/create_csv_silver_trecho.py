import sys
sys.path.append('./')

import pandas as pd
import src.utils.postgresql_utils as puts

#extracting data from raw tables and manipulating to put in silver tables
#insertion of silver_viagem
db_columns = [
    'v.id_viagem',
    't.sequencia_trecho',
    't.origem_data',
    't.origem_uf',
    't.origem_cidade',
    't.destino_data',
    't.destino_uf',
    't.destino_cidade',
    't.meio_transp',
    't.num_diarias'
    ]

offset = 0

#todo: verificar a condição do inner join
while True:
    query = f'''
        SELECT {','.join(db_columns)} FROM raw_trecho t
        INNER JOIN raw_viagem v
            ON t.id_viagem = v.id_viagem
        LIMIT 100000 OFFSET {offset};
        '''

    rows = puts.execute_dql(query)

    if not rows:
        break

    df_chunk = pd.DataFrame(rows, columns=db_columns)

    df_chunk.to_csv(
        './data/silver/silver_trecho.csv',
        mode='w' if offset == 0 else 'a',
        sep=';',
        encoding='latin1',
        index=False,
        header= True if offset == 0 else False
    )

    offset += 100000

    print('lote gravado')

    del df_chunk, rows

#changing Null values from db to NaN
df = pd.read_csv('./data/silver/silver_trecho.csv', sep=';', encoding='latin1')
df = df.replace(['NaN', 'nan', ''], float('nan'))
print(df.info())

#nulls: 763349(total), t.origem_uf(748434), t.destino_uf(748425)

#corrigir tipo:

#df.to_csv('./data/silver/silver_trecho.csv', sep=';', encoding='latin1',  index=False)

