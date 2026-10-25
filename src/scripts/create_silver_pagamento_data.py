import sys
sys.path.append('./')

import pandas as pd
import src.utils.postgresql_utils as puts

#extracting data from raw tables and manipulating to put in silver tables
#insertion of silver_pagamento
db_columns = [
    'p.id_pagamento',
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
        SELECT {','.join(db_columns)} FROM raw_viagem
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

#---------------
#data converting
#---------------

#df = pd.read_csv('./data/silver/silver_pagamento.csv', sep=';', encoding='latin1')

#changing Null values to NaN
#df = df.replace(['NaN', 'nan', ''], float('nan'))

#correction of type numeric
#df ['id_pagamento'] = df['id_pagamento'].str.strip()
#df ['valor'] = df['valor'].str.strip().str.replace(',', '.')
    
#df['id_pagamento'] = pd.to_numeric(df['id_pagamento'], errors='coerce')
#df['valor'] = pd.to_numeric(df['valor'], errors='coerce')

#df.to_csv('./data/silver/silver_pagamento.csv', sep=';', encoding='latin1', index=False)
