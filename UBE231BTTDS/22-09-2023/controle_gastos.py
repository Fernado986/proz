from os import system
from time import sleep

despesas = []
receitas = []

while True:
    system("cls")
    print("[1] - Adicionar Despesa")
    print("[2] - Adicionar Receita")
    print("[3] - Ver Totais")
    print("[4] - Sair")
    opcao = input("Selecione: ")

    if opcao == "1":
        despesas.append(float(input("Informe sua despesa: ")))
        print("\n\nDespesa adicionada com sucesso!")
        sleep(3)

    if opcao == "2":
        receitas.append(float(input("Informe sua receita: ")))
        print("\n\nReceita adicionada com sucesso!")
        sleep(3)

    if opcao == "3":
        print(f"Total de receitas: R${sum(receitas)}")
        print(f"Total de Despesas: R${sum(despesas)}")
        if sum(receitas) < sum(despesas):
            print("\nFalando sério, o trem ta feio!")
        else:
            print("\nElon Musk!")

        input("\n\nPressione qualquer tecla para continuar...")

    if opcao == "4":
        print("Saindo...")
        break
