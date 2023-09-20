# in é uma função para pesquisar se um elemento existe dentro da lista
# index retorna a posição do elemento dentro da lista
# len retorna a quantidade de elementos detro da lista
# append adiciona valores a uma lista


nomes = ["José", "Carlos", "João", "Lenício", "Joana", "Fabiana", "Zé Alfredo"]
proc = input("Informe o nome a ser pesquisado: ")

# for nome in nomes:
#     if nome == proc:
#         print("O nome procurado está na lista!")


if proc in nomes:
    i = nomes.index(proc)
    print(f"O nome procurado está na lista, e está na posição {i}")

