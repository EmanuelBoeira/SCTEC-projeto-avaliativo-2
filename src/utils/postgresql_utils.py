import sys
sys.path.append('../../')

import psycopg2
import pandas as pd
from config import POSTGRESQL_CONFIG

def execute_ddl(query:str) -> None:

    '''
    Function to execute data definition query on database configurated in config file.

    Args: 
        query: a string that contains SQL query
    '''

    try:
        conn = psycopg2.connect(
            host = POSTGRESQL_CONFIG['host'],
            port = POSTGRESQL_CONFIG['port'],
            dbname = POSTGRESQL_CONFIG['dbname'],
            user = POSTGRESQL_CONFIG['user'],
            password = POSTGRESQL_CONFIG['password']
        )

        cur = conn.cursor()
        
        if query and query.strip():
            cur.execute(query)
            conn.commit()

        cur.close()
        conn.close()

    except Exception as e:
        print(e)

def execute_dql(query:str) -> list[tuple]:
    
    '''
    Function to execute data query on database configurated in config file.

    Args: 
        query: a string that contains SQL query

    Returns:
        list(tuple)
    '''
    
    try:
        conn = psycopg2.connect(
            host = POSTGRESQL_CONFIG['host'],
            port = POSTGRESQL_CONFIG['port'],
            dbname = POSTGRESQL_CONFIG['dbname'],
            user = POSTGRESQL_CONFIG['user'],
            password = POSTGRESQL_CONFIG['password']
        )

        cur = conn.cursor()

        cur.execute(query)

        return cur.fetchall()

        cur.close()
        conn.close()

    except Error as e:
        print(e)

def batch_insert(table_name:str, db_columns:list, csv_file:str):

    '''
    Function to insert data on table in the database configurated in config file.
    Tha data inserted must be in a csv file and the columns of db must be in the 
    order of the columns of the csv file.

    Args: 
        table: name of the table in db
        db_columns: name of the columns on table orderned by csv file
        csv_file: path to csv file
    '''

    conn = psycopg2.connect(
        host = POSTGRESQL_CONFIG['host'],
        port = POSTGRESQL_CONFIG['port'],
        dbname = POSTGRESQL_CONFIG['dbname'],
        user = POSTGRESQL_CONFIG['user'],
        password = POSTGRESQL_CONFIG['password']
    )

    cur = conn.cursor()

    try:
        for df in pd.read_csv(csv_file, sep=';',  chunksize=5000):
            sql = f'''
                INSERT INTO {table_name} ({', '.join(db_columns)})
                VALUES %s
                '''

            filling_data = df[columns].astype(object).where(pd.notna(df[columns]), None).values.tolist()

            execute_values(cur, sql, filling_data)

            conn.commit()

    except Exception as e:
        conn.rollback()
        print(e)

    finally:
        cur.close()
        conn.close()

# connection test
#print(execute_dql('select current_database();'))
