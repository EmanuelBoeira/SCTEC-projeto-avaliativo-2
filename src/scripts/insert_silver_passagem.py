import sys
sys.path.append('./')

import pandas as pd
import src.utils.postgresql_utils as puts

df = pd.read_csv('./data/silver/silver_passagem.csv', sep=';', encoding='latin1')

#changing Null values to NaN
df = df.replace(['NaN', 'nan', ''], float('nan'))

#remove duplicates
#print(df.duplicated().sum()) #99991 duplicatas
df.drop_duplicates(inplace=True)

#filling null values
#origem_ida_uf(3826 ausentes): preencher com 'desconhecido'
df['p.origem_ida_uf'].fillna('desconhecido', inplace=True)

#destino_ida_uf(4619 ausente): preencher com 'desconhecido'
df['p.destino_ida_uf'].fillna('desconhecido', inplace=True)

#the null values of p.data_compra was keeped

#correction of type datetime
df['p.data_compra'] = pd.to_datetime(df['p.data_compra'], format='%d/%m/%Y', errors='coerce')

#correction of type numeric
df['p.valor_passagem'] = pd.to_numeric(df['p.valor_passagem'].astype('string').str.strip().str.replace(',','.'), errors='coerce')
df['p.taxa_servico'] = pd.to_numeric(df['p.taxa_servico'].astype('string').str.strip().str.replace(',','.'), errors='coerce')

df.to_csv('./data/silver/silver_passagem.csv', sep=';', encoding='latin1', index=False)

columns = [
    'id_viagem',
    'meio_transporte',
    'pais_origem_ida',
    'uf_origem_ida',
    'cidade_origem_ida',
    'pais_destino_ida',
    'uf_destino_ida',
    'cidade_destino_ida',
    'valor_passagem',
    'taxa_servico',
    'data_emissao'
    ]

puts.batch_insert('silver_passagem', columns, './data/silver/silver_passagem.csv')
