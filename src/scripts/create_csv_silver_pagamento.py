import sys
sys.path.append('./')

import pandas as pd
import src.utils.postgresql_utils as puts

#extracting data from raw tables and manipulating to put in silver tables
#insertion of silver_pagamento
db_columns = [
    'v.id_viagem',
    'p.num_proposta',
    'p.nome_orgao_pagador',
    'p.nome_un_gestora_pagadora',
    'p.tipo_pagamento',
    'p.valor'
    ]

#execute the query in chunks of 100000 lines to not overload RAM
offset = 0

while True:
    query = f'''
        SELECT {','.join(db_columns)}
        FROM raw_pagamento p
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
        './data/silver/silver_pagamento.csv',
        mode='w' if offset == 0 else 'a',
        sep=';',
        encoding='latin1',
        index=False,
        header= True if offset == 0 else False
    )

    offset += 100000

    print('lote gravado!')
    
    del df, rows
