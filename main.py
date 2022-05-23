
from acesso_cep import BuscaEndereco
from CPF_CNPJ import Documento
from CPF_CNPJ import CNPJ
from TelefonesBr import TelefonesBr
from Data_Br import DatasBr


# Valida CEP
cep = "01001000"
objeto_cep = BuscaEndereco(cep)
bairro, cidade, uf = objeto_cep.acessa_via_cep()
print(bairro, cidade, uf)


# Valida CPF
cpf_um = "15316264754"
documento = Documento.cria_documento(cpf_um)
print(documento)


# Valida Telefone
telefone = "552126481234"
telefone_objeto = TelefonesBr(telefone)
print(telefone_objeto)


# Valida Data
hoje = DatasBr()
print(hoje.tempo_cadastro())
