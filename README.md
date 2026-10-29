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

## Objetivo do projeto

  O projeto busca analisar dados brutos desponibilizados em arquivo csv e reponder as seguintes perguntas:

  - Quais os 5 órgãos com maior curto total?
  - Quais os 3 destinos com maior custo médio por viagem?
  - Qual a viagem com maior duração e seu custo?
  - Qual o tipo de pagamento com maior custo médio?
  - Qual o meio de transporte mais usado em trechos?
  - Qual UF de destino aparece mais em trechos?
  - Qual órgão pagou mais no total?

# Dependencias
    
  - python-dotenv
  - psycopg2
  - pandas
  - matplotlib

# Forma de execução

  Antes de executar qualquer script, crie um Banco de Dados e insira os seus valores no arquvo .env criado como no exemplo .env-example.

  Execute o script `main.py` no diretório raiz do projeto, como no exemplo a seguir, e prossiga conforme o script pedir:

  `python main.py`
  

# Sequência recomendada de execução no script main.py

  Após executar o `main.py` digite os comandos em ordem crescente 1 -> 2 -> 3 -> 4 ou digite 5 e aperte Enter.


# Resultado da análise

  - Quais os 5 órgãos com maior curto total?

    - Ministério da defesa - gastou R$ 261.287,40
    - Ministério de minas e energia - gastou R$ 245.852,80
    - Ministério da justiça e segurança pública - gastou R$ 216.728,36

  - Quais os 3 destinos com maior custo médio por viagem?

    - Brasil - custo de R$ 126.214,70
    - China - custo de R$ 112.870,41
    - Estados Unidos da América - custo de R$ 86.678,04

  - Qual a viagem com maior duração e seu custo?

    - viagem com id = 20699856 - duração de 383 dias

  - Qual o tipo de pagamento com maior custo médio?
  - Qual o meio de transporte mais usado em trechos?
  - Qual UF de destino aparece mais em trechos?
  - Qual órgão pagou mais no total?
