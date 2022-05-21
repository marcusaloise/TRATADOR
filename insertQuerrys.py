import connection_db 



def botadora(row, adress):
    con =  connection_db.conecta_pg()
    insert = con.cursor()
    insert.execute("INSERT INTO bairros (cep, bairro) VALUES ({}, '{}')".format(row,adress))
    con.commit()
    insert.close()
    con.close()
    return insert
    