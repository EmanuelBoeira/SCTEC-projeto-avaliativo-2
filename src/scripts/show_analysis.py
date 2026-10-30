import sys
sys.path.append('./')

import src.utils.postgresql_utils as puts

import pandas as pd
import matplotlib.pyplot as plt

#TODO:
# - deixar o plot mais bonito

def show_analysis() -> bool:
    '''
    Prints and plot the analysis that answers the projects questions.

    Args:
        None

    Returns:
        bool
    '''

    try:
        #Quais os 5 orgãos com maior custo total?
        columns = [
            'CÓD. ORGÃO SUPERIOR',
            'NOME ORGÃO SUPERIOR',
            'VALOR TOTAL GASTO'
            ]

        query = '''
            SELECT * FROM gold_orgao_custo;
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
            SELECT * FROM gold_custo_viagem;
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
            SELECT * FROM gold_maior_duracao;
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
        fig, ax = plt.subplots(4, figsize=(12,14), constrained_layout = True)
        fig.set_facecolor('0.9')

        #Qual o tipo de pagamento com maior valor médio?
        query = '''
            SELECT * FROM gold_tipo_pagamento;
            '''

        results = puts.execute_dql(query)[:5][::-1]

        x = [result[0].upper() for result in results]
        y = [result[1] for result in results]

        ax[0].barh(x, y)
        ax[0].set_title('Qual o tipo de pagamento com maior valor médio?')
        ax[0].set_xlabel('Valor médio (R$)')
        #ax[0].set_ylabel('Tipo de pagamentos')

        results.clear()
        x.clear()
        y.clear()

        #Qual o meio de teansporte mais usado nos trechos?
        query = '''
            SELECT * FROM gold_transporte_trecho;
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
            SELECT * FROM gold_UF_trecho;
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
            SELECT * FROM gold_orgao_gastou;
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

        plt.savefig('./outputs/plots-analysis.png')

        plt.show()

        return True

    except Exception as e:
        print(f'\n{e}\n')

        return False
