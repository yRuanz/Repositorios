from Classe import *

user01 = Cadastro_user("Ruan", 16)
user01.inserir_endereco("Jundiaí", " SP")

print(user01.getNome)
print(user01.getIdade())
print(user01.getEndereco().getCidade())
print(user01.getEstado().getEstado())