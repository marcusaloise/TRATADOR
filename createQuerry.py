import connection_db

# Vai direcionar aonde esta os ceps
def buscaCep():
    cur = connection_db.conecta_oracle().cursor()
    cur.execute("Aqui vai o select para o banco")
    return cur


