import sys
sys.path.append('./')

import pandas as pd
import src.utils.postgresql_utils as puts

def insert_silver_passagem() -> None:
    '''
    Reads data from raw_passagem, creates a csv file in ./data/silver/
    and inserts this cleaned data on silver_passagem.

    Args:
        None

    Retuens:
        bool
    '''

    try:
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

        #----------------
        # Data convertion
        #----------------

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

        return True

    except Exception as e:
        print(f'\n{e}\n')

        return False
