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
