from os import system

lista = []

while True:
    system("cls")

    print("[ 1 ] - Adicionar")
    print("[ 2 ] - Listar")
    print("[ 3 ] - Sair")

    opcao = input("Selecione: ")

    if opcao == "1":
        lista.append(input("Insira o item: "))

    elif opcao == "2":

        for i in range(len(lista)):
            print(f"- {lista[i]}")

        input("\nPressione qualquer tecla para continuar...")

    elif opcao == "3":
        print("Saindo!")
        break

    else:
        print("Opção Inválida!")
        input("Pressione qualquer tecla para continuar...")
