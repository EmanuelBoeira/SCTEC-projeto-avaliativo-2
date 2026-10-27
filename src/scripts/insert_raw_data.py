import sys
sys.path.append('./')

import src.utils.postgresql_utils as puts
#import pandas as pd

#insert on raw_viagem
columns = [
    'id_viagem',
    'num_proposta',
    'situacao',
    'urgente',
    'justificativa_urgente',
    'cod_orgao_superior',
    'nome_orgao_superior',
    'cod_orgao_solicitante',
    'nome_orgao_solicitante',
    'cpf',
    'nome',
    'cargo',
    'funcao',
    'descricao_funcao',
    'data_inicio',
    'data_fim',
    'destinos',
    'motivo',
    'valor_diarias',
    'valor_passagens',
    'valor_devolucao',
    'valor_outros'
    ]

puts.batch_insert('raw_viagem', columns, 'data/raw/2025_Viagem.csv')

#insert on raw_trecho
columns = [
    'id_viagem',
    'num_proposta',
    'sequencia_trecho',
    'origem_data',
    'origem_pais',
    'origem_uf',
    'origem_cidade',
    'destino_data',
    'destino_pais',
    'destino_uf',
    'destino_cidade',
    'meio_transp',
    'num_diarias',
    'missao'
    ]

puts.batch_insert('raw_trecho', columns, 'data/raw/2025_Trecho.csv')

#insert on raw_passagem
columns = [
    'id_viagem',
    'num_proposta',
    'meio_transp',
    'origem_ida_pais',
    'origem_ida_uf',
    'origem_ida_cidade',
    'destino_ida_pais',
    'destino_ida_uf',
    'destino_ida_cidade',
    'origem_volta_pais',
    'origem_volta_uf',
    'origem_volta_cidade',
    'destino_volta_pais',
    'destino_volta_uf',
    'destino_volta_cidade',
    'valor_passagem',
    'taxa_servico',
    'data_compra',
    'hora_compra'
    ]

puts.batch_insert('raw_passagem', columns, 'data/raw/2025_Passagem.csv')

#insert on raw_pagamento
columns = [
    'id_viagem',
    'num_proposta',
    'cod_orgao_superior',
    'nome_orgao_superior',
    'cod_orgao_pagador',
    'nome_orgao_pagador',
    'cod_un_gestora_pagadora',
    'nome_un_gestora_pagadora',
    'tipo_pagamento',
    'valor'
    ]

puts.batch_insert('raw_pagamento', columns, 'data/raw/2025_Pagamento.csv')
