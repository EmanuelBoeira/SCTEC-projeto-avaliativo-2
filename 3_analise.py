import src.scripts.show_analysis as analysis
import src.scripts.create_gold as cgold

def analise():
    if cgold.create_gold():
        if analysis.show_analysis():
            print('\tFim da análise')

        else:
            print('\tErro ao executar show_analysis.py')
    else:
        print('\tfalha ao criar GOLD')

analise()
