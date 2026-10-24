# Autor: Emanuel Boeira Martins
 

# Introdução

Este projeto foi realizado como atividade avaliativa para o curso de Análise de Dados com Python oferecido pelo SCTEC em parceria com o SENAI.
O projeto busca realizar uma análise exploratória de dados a partir do SGBD PostgreSQL integrado pela linguagem Python.
Os dados foram obtidos pelos arquivos .csv pelo link: ... e foram inseridos no banco de dados.


# Sobre o Projeto

    - Todos os scripts estão dentro de src/
    - Em src/utils/ há scripts com funções que foram usadas em outro locais
    - Em src/scripts/ estão os scripts principais, responsáveis por criar as tabelas, e inserir dados no banco de dados
    - O arquivo config.py é responsável por fornecer a configuração das variáveis de conexão com o Banco de Dados, essas variáveis estão definidas em .env
    - O arquivo .env-example é um exemplo  de como o .env deve ser preenchido (use os valores correspondentes à sua máquina)
    - Este projeto cria as tabelas no Banco de Dados, mas não o cria, então execute `CREATE DATABASE db_name` antes dos scripts


# Dependencias
    
    - python-dotenv
    - psycopg2
    - pandas
    - matplotlib

# Forma de execução

    Execute todos os scripts a partir o diretório raiz do projeto, como no exemplo a seguir:

    `python src/scripts/create_tables.py` (cria as tabelas no Banco de Dados)

# Sequência recomendada de execução
