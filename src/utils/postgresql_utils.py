import sys
sys.path.append('../../')

import psycopg2
from config import POSTGRESQL_CONFIG

def execute_ddl(query) -> None:

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

        cur.execute(query)

        cur.close()
        conn.close()

    except Error as e:
        print(e)

def execute_dql(query) -> list[tuple]:
    
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

# connection test
#print(execute_dql('select current_database();'))
