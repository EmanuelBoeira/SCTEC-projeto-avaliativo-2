import src.scripts.insert_raw_data as ird
from dotenv import load_dotenv
import os
import gdown
import zipfile

load_dotenv()

url = os.environ.get('DATA_LINK')

def extrair():

    gdown.download(url, 'data/raw/dados.zip', quiet=False)

    with zipfile.ZipFile('data/raw/dados.zip', 'r') as zip_ref:
        zip_ref.extractall('data/raw/')

    if ird.insert_raw_data():
        print('\tDados extraídos dos arquivos CSV e inseridos nas tabelas RAW')

    else:
        print('\tfalha ao extrair dados dos arquivos CSV')

extrair()
