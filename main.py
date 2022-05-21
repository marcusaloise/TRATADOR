import createQuerry
import tiraCarater
import _API_
import insertQuerrys

# Vai listar todos os cep do banco
cur = createQuerry.buscaCep()
while True:
    row = cur.fetchone()
    
    row = tiraCarater.tirarCaracter(row)
    try:
        address = _API_.buscadinha(row)
        
        print(row, address['bairro'])
        insertQuerrys.botadora(row, address['bairro'])
    except:
        print('')
    
    if row is None:
        cur.close()
        break
    #print(row)