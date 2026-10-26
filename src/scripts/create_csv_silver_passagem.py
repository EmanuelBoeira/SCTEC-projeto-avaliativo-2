import sys
sys.path.append('./')

import pandas as pd
import src.utils.postgresql_utils as puts

#extracting data from raw tables and manipulating to put in silver tables
#insertion of silver_passagem
db_columns = [
    'v.id_viagem',
    'p.meio_transp',
    'p.origem_ida_pais',
    'p.origem_ida_uf',
    'p.origem_ida_cidade',
    'p.destino_ida_pais',
    'p.destino_ida_uf',
    'p.destino_ida_cidade',
    'p.valor_passagem',
    'p.taxa_servico',
    'p.data_compra'
    ]

#execute the query in chunks of 100000 lines to not overload RAM
offset = 0

while True:
    query = f'''
        SELECT {','.join(db_columns)}
        FROM raw_passagem p
        INNER JOIN raw_viagem v
            ON v.id_viagem = p.id_viagem
        ORDER BY v.id_viagem ASC
        LIMIT 100000 OFFSET {offset};
        '''
    rows = puts.execute_dql(query)

    if not rows:
        break

    #creates a dataframe from the query above
    df = pd.DataFrame(rows, columns=db_columns)

    #creates and append data from the chunk
    df.to_csv(
        './data/silver/silver_passagem.csv',
        mode='w' if offset == 0 else 'a',
        sep=';',
        encoding='latin1',
        index=False,
        header= True if offset == 0 else False
    )

    offset += 100000

    print('lote gravado!')
    
    del df, rows
