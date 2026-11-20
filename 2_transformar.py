import src.scripts.insert_silver_pagamento
import src.scripts.insert_silver_passagem
import src.scripts.insert_silver_trecho
import src.scripts.insert_silver_viagem

def transformar():
    
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

transformar()
