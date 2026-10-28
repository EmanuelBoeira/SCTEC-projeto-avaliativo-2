import sys
sys.path.append('./')

import pandas as pd
import src.utils.postgresql_utils as puts

def insert_silver_trecho() -> bool:
    '''
    Reads data from raw_trecho, creates a csv file in ./data/silver/
    and inserts this cleaned data on silver_trecho.

    Args:
        None

    Retuens:
        bool
    '''

    try:
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
                SELECT {','.join(db_columns)} 
                FROM raw_trecho t
                INNER JOIN raw_viagem v
                    ON t.id_viagem = v.id_viagem
                ORDER BY t.id_viagem ASC
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

        #----------------
        # Data convertion
        #----------------

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

        puts.batch_insert('silver_trecho', columns, './data/silver/silver_trecho.csv')

        return True

    except Exception as e:
        print(f'\n{e}\n')

        return False
