import sys
sys.path.append('./')

import pandas as pd
import src.utils.postgresql_utils as puts

df = pd.read_csv('./data/silver/silver_trecho.csv', sep=';', encoding='latin1')

#changing Null values to NaN
df = df.replace(['NaN', 'nan', ''], float('nan'))

#duplicates
#print(df.duplicated().sum()) #99991 duplicatas
df.drop_duplicates(inplace=True)
df.drop_duplicates(subset=['t.sequencia_trecho'], inplace=True)

#origem_uf(12960 ausentes): preencher com 'desconhecido'
df['t.origem_uf'].fillna('desconhecido', inplace=True)

#destino_uf(12949 ausente): preencher com 'desconhecido'
df['t.destino_uf'].fillna('desconhecido', inplace=True)

#correction of type datetime
df['t.origem_data'] = pd.to_datetime(df['t.origem_data'], format='%d/%m/%Y', errors='coerce')
df['t.destino_data'] = pd.to_datetime(df['t.destino_data'], format='%d/%m/%Y', errors='coerce')

#correction of type numeric
df['t.num_diarias'] = pd.to_numeric(df['t.num_diarias'].astype('string').str.strip().str.replace(',','.'), errors='coerce')
#print(df.info())

df.to_csv('./data/silver/silver_trecho.csv', sep=';', encoding='latin1', index=False)

columns = [
    'id_viagem',
    'sequencia_trecho',
    'origem_data',
    'origem_uf',
    'origem_cidade',
    'destino_data',
    'destino_uf',
    'destino_cidade',
    'meio_transporte',
    'numero_diarias'
    ]

#verificar silver_viagem(id_viagem=20834461), ele existe no raw, mas não em silver_viagem
puts.batch_insert('silver_trecho', columns, './data/silver/silver_trecho.csv')
