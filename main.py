import psycopg2
import pandas as pd
from IPython.display import display

connection =  psycopg2.connect(
    host = 'localhost',
    database = 'GlobalSales',
    user = 'postgres',
    password = '7880'
)
cursor = connection.cursor()

cursor.execute("SELECT * FROM vendas_globais")
results = cursor.fetchall()

df = pd.DataFrame(results, columns=[desc[0] for desc in cursor.description]) 
display(df) 

cursor.close()
connection.close()