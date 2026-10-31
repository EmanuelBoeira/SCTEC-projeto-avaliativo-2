# Autor: Emanuel Boeira Martins
 

# Introdução

Este projeto foi realizado como atividade avaliativa para o curso de Análise de Dados com Python oferecido pelo SCTEC em parceria com o SENAI.
O projeto busca realizar uma análise exploratória de dados a partir do SGBD PostgreSQL integrado pela linguagem Python.
Os dados foram obtidos pelos arquivos .csv pelo link: https://drive.google.com/drive/folders/1nMd1o8mm_KhfnIcByVf7Tv--NeY08t7_ e foram inseridos no banco de dados.


# Sobre o Projeto

  - Todos os scripts estão dentro de src/ com exceção do main.py
  - Em src/utils/ há scripts com funções que foram usadas em outros locais
  - Em src/scripts/ estão os scripts principais, responsáveis por criar as tabelas, e inserir dados no banco de dados
  - O arquivo config.py é responsável por fornecer a configuração das variáveis de conexão com o Banco de Dados, essas variáveis estão definidas em .env
  - O arquivo .env-example é um exemplo  de como o .env deve ser preenchido (use os valores correspondentes à sua máquina)
  - Este projeto cria as tabelas no Banco de Dados, mas não o cria, então execute `CREATE DATABASE db_name` antes dos scripts
  - O diretório ./outputs/ armazena o arquivo plots-analysis.png, que é a imagem contendo os gráficos da análise

# Descrição dos arquivos de ./src/scripts/

  | arquivo | descrição |
  | --- | --- |
  | create_tables.sql | Script SQL usado em create_tables.py para criar tabelas raw e silver |
  | create_tables.py | Criação de 8 tabelas no banco de dados definido no .env |
  | insert_raw_data.py | Insere os dados presentes nos arquivos csv em ./data/raw/ nas 4 tabelas raw |
  | insert_silver_viagem.py | Extrai os dados da tabela raw_viagem, faz os devidos tratamentos, salva em um arquivo csv em ./data/silver/ e inseri na tabela silver_viagem |
  | insert_silver_trecho.py | Extrai os dados da tabela raw_trecho, faz os devidos tratamentos, salva em um arquivo csv em ./data/silver/ e inseri na tabela silver_trecho |
  | insert_silver_passagem.py | Extrai os dados da tabela raw_passagem, faz os devidos tratamentos, salva em um arquivo csv em ./data/silver/ e inseri na tabela silver_passagem |
  | insert_silver_pagamento.py | Extrai os dados da tabela raw_pagamento, faz os devidos tratamentos, salva em um arquivo csv em ./data/silver/ e inseri na tabela silver_pagamento |
  | create_gold.py | Criação das VIEWs gold que respondem as perguntas do projeto |
  | show_analysis.py | Lê os dados preentes nas VIEWs gold e mostra as 3 primeiras no terminal e as 4 últimas em forma de gráficos |


# Objetivo do projeto

  O projeto busca analisar dados brutos desponibilizados em arquivo csv e reponder as seguintes perguntas utilizando a arquiterira Medallion (Bronze/Raw, Silver, Gold):

  - Quais os 5 órgãos com maior custo total?
  - Quais os 3 destinos com maior custo médio por viagem?
  - Qual a viagem com maior duração e seu custo?
  - Qual o tipo de pagamento com maior custo médio?
  - Qual o meio de transporte mais usado em trechos?
  - Qual UF de destino aparece mais em trechos?
  - Qual órgão pagou mais no total?


# Dependencias

  - Python 3.10 ou superior    
  - python-dotenv
  - psycopg2
  - pandas
  - matplotlib


# Forma de execução

  Antes de executar qualquer script, certifique-se de: 
  
  - Instalar as dependências
  
  - Criar o Banco de Dados e inserir os seus valores no arquvo .env criado como no exemplo .env-example. 

  -  É necessário criar os diretórios ./data ./data/raw/ e ./data/silver/ 

  -  Os arquivos .csv brutos devem ser colocados em ./data/raw/

  -  Evite executar os scripts em ./src/scripts/ individualmente, pois a ordem da execução pode influenciar os resultados.

  Execute o script `main.py` no diretório raiz do projeto, como no exemplo a seguir, e prossiga conforme o script pedir:

  `python main.py`
  

# Sequência recomendada de execução no script main.py

  Após executar o `main.py` digite os comandos em ordem crescente 1 -> 2 -> 3 -> 4 -> 5 ou digite 6 e aperte Enter.

  OBS.: 
  - As etapas 2 e 3 do script main.py costuma demorar alguns segundos para finalizar sua execução devido à manipulação e insersão de dados.

  - Ao selecionar a opção 5, um arquivo plots-analysis.png será criado ou sobreescrito em ./outputs/


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
 
    &nbsp; Viagem com id = 20699856 - duração de 383 dias


  - Qual o tipo de pagamento com maior custo médio?

    &nbsp; Pelo primeiro gráfico é possível perceber que PASSAGEM é o maior custo médio.


  - Qual o meio de transporte mais usado em trechos?

    &nbsp; Pelo segundo gráfico é possível perceber que VEÍCULO PRÓPRIO é o meio de transporte mais usado nos trechos.


  - Qual UF de destino aparece mais em trechos?

    &nbsp; Pelo terceiro gráfico é possível perceber que Destrito Federal é a UF que mais aparece em trechos.


  - Qual órgão pagou mais no total?

    &nbsp; Pelo quarto gráfico é possível perceber que o órgão sigiloso tem o maior custo total, mas essa opção pode 
    representar mais de um órgão, então o órgão com maior custo total é o FUNDO NACIONAL DE SEGURANÇA.
