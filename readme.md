# importando os dados do banco para o python

import biblioteca psycopg2 para conectar no banco de dados postgres
import biblioteca pandas que fornece o DataFrame
from IPython exibi a interação dos dados no ambiente do jupyter e import display para exibir os dados do df

após impotar a biblioteca psycopg2 e conectar ao banco

criar um objeto 'cursor' que é usado pra executar comandos SQL no banco de dados 

usando o objeto cursor pode se usar a função exectar para excutar diferentes comandos em SQL como por exemplo: cursor.execute(SELECT * FROM nome_da_tabela)

fetchall trás um resultado atráves da consulta SQL e armazena em uma variável 

df resulta dados do dataframe do pandas que cria uma lista de nomes de colunas, extraida do cursor.description que retorna informações dos dados

o display(df) vai exibir os dados do dataframe dentro do ambientte do Jupyther(Ipython)

por fim, fechar os métodos