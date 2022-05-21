import psycopg2
import cx_Oracle

# realizando a conexão no banco infomed

def conecta_oracle():
    cx_Oracle.init_oracle_client(lib_dir=r"C:\oracle\instantclient_21_3")
    conn = cx_Oracle.connect(user="***********", password="********", dsn="*******", encoding="UTF-8")
    return conn




def conecta_pg():
  conn = psycopg2.connect(host='*******', 
                         database='*****',
                         user='*******', 
                         password='******')
  return conn

# print(conecta_db())








