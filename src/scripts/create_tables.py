import sys
sys.path.append('../utils/')

import postgresql_utils as pu

with open('create_tables.sql', 'r', encoding='utf-8') as file:
    file_content = file.read()

commands = file_content.split(';')
#print(file_content)

for command in commands:
    command.strip()
    #print(command)
    if command:
        pu.execute_ddl(command)
