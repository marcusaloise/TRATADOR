from pycep_correios import get_address_from_cep, WebService
def buscadinha(row):
    address = get_address_from_cep(f'{row}' , webservice=WebService.CORREIOS)
    return address
#print(buscadinha('76804060'))
