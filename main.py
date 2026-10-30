import src.scripts.create_tables
import src.scripts.insert_raw_data
import src.scripts.insert_silver_viagem
import src.scripts.insert_silver_trecho
import src.scripts.insert_silver_passagem
import src.scripts.insert_silver_pagamento
import src.scripts.create_gold
import src.scripts.show_analysis

while True:

    print('''
        Digite um dos números abaixo:

        1 - Criar tabelas no banco de dados.
        2 - Inserir dados brutos nas tabelas raw(Bronze).
        3 - Inserir dados tratados nas tabelas Silver.
        4 - Criar camada gold da análise.
        5 - Mostrar análise de dados.
        6 - Executar todo o projeto, do início ao fim.
        0 - Sair.
        ''')

    user_input = input('\n\tDigite um dos números acima: ')[0]

    match user_input:
        case '0':
            break

        case '1':
            if src.scripts.create_tables.create_tables():
                print('\tTabelas criadas com sucesso!')
            else:
                print('\tFalha ao criar tabelas!')

        case '2':
            if src.scripts.insert_raw_data.insert_raw_data():
                print('\tDados inseridos em raw!')
            else:
                print('\tFalha ao inserir dados!')

        case '3':
            if src.scripts.insert_silver_viagem.insert_silver_viagem():
                print('\tDados inseridos em silver_viagem')
            else:
                print('\tFalha ao inserir dados em silver_viagem')

            if src.scripts.insert_silver_trecho.insert_silver_trecho():
                print('\tDados inseridos em silver_trecho')
            else:
                print('\tFalha ao inserir dados em silver_trecho')

            if src.scripts.insert_silver_passagem.insert_silver_passagem():
                print('\tDados inseridos em silver_passagem')
            else:
                print('\tFalha ao inserir dados em silver_passagem')

            if src.scripts.insert_silver_pagamento.insert_silver_pagamento():
                print('\tDados inseridos em silver_pagamento')
            else:
                print('\tFalha ao inserir dados em silver_pagamento')

        case '4':
            if src.scripts.create_gold.create_gold():
                print('\tCamada gold criada')
            else:
                print('\tFalha ao executar create_gold.py')

        case '5':
            if src.scripts.show_analysis.show_analysis():
                print('\tFim da análise')
            else:
                print('\tFalha ao executar show_analysis.py')

        case '6':
            src.scripts.create_tables.create_tables()
            src.scripts.insert_raw_data.insert_raw_data()
            src.scripts.insert_silver_viagem.insert_silver_viagem()
            src.scripts.insert_silver_trecho.insert_silver_trecho()
            src.scripts.insert_silver_passagem.insert_silver_passagem()
            src.scripts.insert_silver_pagamento.insert_silver_pagamento()
            src.scripts.create_gold.create_gold()
            src.scripts.show_analysis.show_analysis()

        case _:
            print('\n\tValor incorreto! Digite uma das opções abaixo.\n')
