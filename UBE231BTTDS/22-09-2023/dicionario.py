from os import system

lista_cadastro = []
comando = ""

while True:
    system("cls")
    cadastro = {"nome": input("Informe o seu nome: "),
                "idade": int(input("Informe a sua idade: ")),
                "altura": float(input("Informe sua altura: ")),
                "signo": input("Informe o seu signo: ")}

    lista_cadastro.append(cadastro)
    print("\nCadastro realizado com sucesso!")

    comando = input("\n\nPara encerrar, digite Sair: ")
    if comando.lower() == "sair":
        break


while True:
    nome_procurado = input("Informe o nome que você quer procurar: ")

    for item in lista_cadastro:
        if item["nome"] == nome_procurado:
            print("O nome está na lista de cadastro!")
            break
        else:
            print("O nome não foi encontrado na lista.")

        comando = input("\n\nPara encerrar, digite Sair: ")
        if comando.lower() == "sair":
            break
