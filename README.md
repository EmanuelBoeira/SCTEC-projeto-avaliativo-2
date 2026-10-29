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

# Objetivo do projeto

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

  - Quais os 5 órgãos com maior custo total?

    - Ministério da justiça e segurança pública - gastou R$ 490.813.474,85
    - Ministério da defesa - gastou R$ 157.059.698,59
    - Ministério da Educação - gastou R$ 112.519.456,96
    - Ministério do Meio Ambiente e Mudança do Clima - gastou R$ 50.548.377,44
    - Ministério da Previdência Social - gastou R$ 40.921.476,10


  - Quais os 3 destinos com maior custo médio por viagem?

    - Brasil - custo de R$ 126.214,70
    - China - custo de R$ 112.870,41
    - Estados Unidos da América - custo de R$ 86.678,04


  - Qual a viagem com maior duração e seu custo?

    - viagem com id = 20699856 - duração de 383 dias


  - Qual o tipo de pagamento com maior custo médio?

    Pelo primeiro gráfico é possível perceber que PASSAGEM é o meior custo médio.


  - Qual o meio de transporte mais usado em trechos?

    Pelo segundo gráfico é possível perceber que VEÍCULO PRÍPRIO é o meio de transporte mais usado nos trechos.


  - Qual UF de destino aparece mais em trechos?

    Pelo terceiro gráfico é possível perceber que Destrito Federal é a UF que mais aparece em trechos.


  - Qual órgão pagou mais no total?

    Pelo quarto gráfico é possível perceber que o órgão sigiloso tem o maior custo total, mas essa opção pode 
    representar mais de um órgão, então o órgão com maior custo total é o FUNDO NACIONAL DE SEGURANÇA.
