import sys
sys.path.append('./')

import src.utils.postgresql_utils as puts

def create_tables() -> bool:
    '''
    Creates 8 tables on database defined in dotenv file. 4 tables raw and 4 tables silver.

    Args:
        None

    Returns:
        bool
    '''

    try:
        with open('./src/scripts/create_tables.sql', 'r', encoding='utf-8') as file:
            file_content = file.read()

        commands = file_content.split(';')

        for command in commands:
            command.strip()
            if command:
                puts.execute_ddl(command)

        return True

    except Exception as e:
        print(f'\n{e}\n')

        return False
