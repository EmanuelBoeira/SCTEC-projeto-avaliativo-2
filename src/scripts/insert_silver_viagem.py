import sys
sys.path.append('./')

import pandas as pd
import src.utils.postgresql_utils as puts

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
