import sys
sys.path.append('./')
#sys.path.append('./src/utils/')
#sys.path.append('./src/scripts/')

import src.utils.postgresql_utils as puts

with open('./src/scripts/create_tables.sql', 'r', encoding='utf-8') as file:
    file_content = file.read()

commands = file_content.split(';')

for command in commands:
    command.strip()
    if command:
        puts.execute_ddl(command)
