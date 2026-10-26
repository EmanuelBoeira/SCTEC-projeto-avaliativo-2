import sys
sys.path.append('./')

import pandas as pd
import src.utils.postgresql_utils as puts

df = pd.read_csv('./data/silver/silver_pagamento.csv', sep=';', encoding='latin1')

#changing Null values to NaN
df = df.replace(['NaN', 'nan', ''], float('nan'))

#remove duplicates
#print(df.duplicated().sum()) #99991 duplicatas
df.drop_duplicates(inplace=True)

#have no null values
df['p.valor'] = pd.to_numeric(df['p.valor'].astype('string').str.strip().str.replace(',','.'), errors='coerce')

df.to_csv('./data/silver/silver_pagamento.csv', sep=';', encoding='latin1', index=False)

columns = [
    'id_viagem',
    'num_proposta',
    'nome_orgao_pagador',
    'nome_ug_pagadora',
    'tipo_pagamento',
    'valor'
    ]

puts.batch_insert('silver_pagamento', columns, './data/silver/silver_pagamento.csv')
