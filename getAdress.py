import connection_db
from pycep_correios import get_address_from_cep, WebService


address = get_address_from_cep('76820132' , webservice=WebService.VIACEP)

print(address)

# API para verificaw1r os os dados do CEP