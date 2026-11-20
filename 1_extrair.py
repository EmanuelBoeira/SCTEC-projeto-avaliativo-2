import src.scripts.insert_raw_data as ird

def extrair():
    if ird.insert_raw_data():
        print('\tDados extraídos dos arquivos CSV e inseridos nas tabelas RAW')

    else:
        print('\tfalha ao extrair dados dos arquivos CSV')

extrair()
