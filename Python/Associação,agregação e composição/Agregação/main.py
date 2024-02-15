from classes import *

n1 = Produtos("Notebook", 4500)

n2 = Produtos("Iphone", 800)

n3 = Produtos("Tablet", 2500)

Carrinho_Carlos = Carrinho_Compra()

Carrinho_Carlos.inserir_produto(n1)

#print({Carrinho_Carlos.lista_compra[0].getNome()})

print(Carrinho_Carlos.getLista(0).getNome())
print(Carrinho_Carlos.getLista(0).getValor())

print("------------------------------------------------")

Carrinho_Carlos.inserir_produto(n2)
Carrinho_Carlos.inserir_produto(n2)
Carrinho_Carlos.inserir_produto(n3)

Carrinho_Carlos.listar_produtos()

print("------------------------------------------------")

Carrinho_Carlos.delProduto(2)
Carrinho_Carlos.listar_produtos()