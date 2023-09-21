from os import system

lista = ["Abacaxi", "Melão", "Uva", "Morango"]

while True:
    system("cls")
    print(lista)
    print("[1] - Adicionar")
    print("[2] - Listar")
    print("[3] - Editar")
    print("[4] - Editar com listagem")
    print("[5] - Encerrar")
    opcao = input("Selecione: ")

    if opcao == "1":
        lista.append(input("Adicione: "))
        input("\n\nPressione qualquer tecla para continuar...")

    elif opcao == "2":
        for item in lista:
            print(f"- {item}")

        input("\n\nPressione qualquer tecla para continuar...")

    elif opcao == "3":
        edicao = input("Informe qual elemento você quer editar: ")

        if edicao in lista:
            indice = lista.index(edicao)

            novo_nome = input("Digite o novo nome: ")
            lista[indice] = novo_nome

            print(f"{novo_nome} editado com sucesso!")
            input("\n\nPressione qualque tecla para continuar...")

        else:
            print("Não existe o elemento informado na lista.")
            input("\n\nPressione qualque tecla para continuar...")

    elif opcao == "4":
        print("\n")

        for item in lista:
            print(f"[{lista.index(item)}] - {item}")

        opcao = int(input("Selecione o item que você quer editar; "))
        novo_nome = input("Informe o novo nome: ")

        lista[opcao] = novo_nome

        input("\n\nPressione qualque tecla para continuar...")

    elif opcao == "5":
        print("Saindo...")
        break

    else:
        print("Opção inválida!")
        input("\n\nPressione qualquer tecla para continuar...")
