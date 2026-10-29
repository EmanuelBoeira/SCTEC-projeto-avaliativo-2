import sys
sys.path.append('./')

import src.utils.postgresql_utils as puts

import pandas as pd
import matplotlib.pyplot as plt

#TODO:
# - criar views ao invez de mostrar dados por df
# - conferir os limit, pois eles podem estar diminuindo as consultas ao invez de mostrar os primeiros valores
# - deixar o plot mais bonito

def data_analysis() -> bool:
    '''
    Prints and plot the analysis that answers the projects questions.

    Args:
        None

    Returns:
        bool
    '''

    try:
        #--------------
        #SQL questions:
        #--------------

        #Quais os 5 orgãos com maior custo total?
        columns = [
            'CÓD. ORGÃO SUPERIOR',
            'NOME ORGÃO SUPERIOR',
            'VALOR TOTAL GASTO'
            ]

        query = '''
            SELECT cod_orgao_superior, nome_orgao_superior, SUM(valor_total) AS soma
            FROM silver_viagem
            GROUP BY cod_orgao_superior, nome_orgao_superior
            ORDER BY soma DESC;
            '''

        df = pd.DataFrame(puts.execute_dql(query), columns=columns)

        print('-'*70)
        print('Quais os 5 orgãos com maior custo total?\n')
        print(df[[columns[1], columns[2]]].head())
        print('-'*70)

        columns.clear()

        #Quais os 3 destinos com maior custo médio por viagem?
        columns = [
            'PAÍS DE DESTINO',
            'UF DE DESTINO',
            'CIDADE DE DESTINO',
            'VALOR MÉDIO'
            ]

        query = '''
            SELECT 
                p.pais_destino_ida,
                p.uf_destino_ida,
                p.cidade_destino_ida,
                ROUND(AVG(v.valor_total), 2) AS media_valor
            FROM silver_viagem v
            INNER JOIN silver_passagem p
                ON v.id_viagem = p.id_viagem
            GROUP BY 
                p.pais_destino_ida,
                p.uf_destino_ida,
                p.cidade_destino_ida
            ORDER BY media_valor DESC;
            '''

        df = pd.DataFrame(puts.execute_dql(query), columns=columns)

        print('-'*50)
        print('Quais os 3 destinos com maior custo médio por viagem?\n')
        print(df[[columns[0], columns[3]]].head(3))
        print('-'*50)

        columns.clear()

        #Qual a viagem com maior duração e seu custo total?
        columns = [
            'ID DA VIAGEM',
            'VALOR TOTAL',
            'QUANT. DE DIAS'
            ]

        query = '''
            SELECT id_viagem, valor_total, duracao_dias
            FROM silver_viagem
            ORDER BY duracao_dias DESC;
            '''

        df = pd.DataFrame(puts.execute_dql(query), columns=columns)

        print('-'*50)
        print('Qual a viagem com maior duração e seu custo total?\n')
        print(df.head(1)) #verificar valores
        print('-'*50)

        columns.clear()

        #---------------------
        #matplotlib questions:
        #---------------------

        #defines a figure with 2 lines and 2 elements in each line
        fig, ax = plt.subplots(4, constrained_layout = True)
        fig.set_facecolor('0.9')

        #Qual o tipo de pagamento com maior valor médio?
        query = '''
            SELECT tipo_pagamento, AVG(valor) as valor_medio
            FROM silver_pagamento
            GROUP BY tipo_pagamento
            ORDER BY valor_medio DESC;
            '''

        results = puts.execute_dql(query)[:5][::-1]

        x = [result[0].upper() for result in results]
        y = [result[1] for result in results]

        results.clear()

        ax[0].barh(x, y)
        ax[0].set_title('Qual o tipo de pagamento com maior valor médio?')
        ax[0].set_xlabel('Valor médio (R$)')
        #ax[0].set_ylabel('Tipo de pagamentos')

        results.clear()
        x.clear()
        y.clear()

        #Qual o meio de teansporte mais usado nos trechos?
        query = '''
            SELECT meio_transporte, COUNT(meio_transporte) AS vezes_usado
            FROM silver_trecho
            GROUP BY meio_transporte
            ORDER BY vezes_usado DESC;
            '''

        results = puts.execute_dql(query)[:5][::-1]

        x = [result[0] for result in results]
        y = [result[1] for result in results]

        ax[1].barh(x, y)
        ax[1].set_title('Qual o meio de teansporte mais usado nos trechos?')
        ax[1].set_xlabel('Quant. de vezes usado')
        #ax[1].set_ylabel('Meios de transporte')

        results.clear()
        x.clear()
        y.clear()

        #Qual UF de destino mais aparece nos trechos?
        query = '''
            SELECT destino_uf, COUNT(destino_uf) AS vezes_repetido
            FROM silver_trecho
            GROUP BY destino_uf
            ORDER BY vezes_repetido DESC;
            '''

        results = puts.execute_dql(query)[:5][::-1]

        x = [result[0] for result in results] 
        y = [result[1] for result in results] 

        ax[2].barh(x, y)
        ax[2].set_title('Qual UF de destino mais aparece nos trechos?')
        ax[2].set_xlabel('Quant. de vezes que aparece')
        #ax[2].set_ylabel('UF - Unidades Federativas')

        results.clear()
        x.clear()
        y.clear()

        #Qual orgão pagou mais no total?
        query = '''
            SELECT nome_orgao_pagador, SUM(valor) AS soma_valor
            FROM silver_pagamento
            GROUP BY nome_orgao_pagador
            ORDER BY soma_valor DESC;
            '''

        results = puts.execute_dql(query)[:5][::-1]

        x = [result[0] for result in results] 
        y = [result[1] for result in results] 

        ax[3].barh(x, y)
        ax[3].set_title('Qual orgão pagou mais no total?')
        ax[3].set_xlabel('Valor pago (R$)')
        #ax[3].set_ylabel('Nome do orgão pagador')

        results.clear()
        x.clear()
        y.clear()


        plt.show()

        return True

    except Exception as e:
        print(f'\n{e}\n')

        return False
