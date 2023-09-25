from os import system
from msvcrt import getch

lista_usuarios = [{'usuario': 'Pedro', 'senha': 'x4grFV0z', 'nivel': 'admin'},
                  {'usuario': 'Luísa', 'senha': 'DldOz0tO', 'nivel': 'admin'},
                  {'usuario': 'Marcelo', 'senha': 'LGLQGKTj', 'nivel': 'admin'},
                  {'usuario': 'Ana', 'senha': 'JmAculhj', 'nivel': 'admin'},
                  {'usuario': 'João', 'senha': 'jTzII2iN', 'nivel': 'gestor'},
                  {'usuario': 'Beatriz', 'senha': 'LP6DDCHV', 'nivel': 'gestor'},
                  {'usuario': 'Roberto', 'senha': 'HT8G7mEP', 'nivel': 'gestor'},
                  {'usuario': 'Fernanda', 'senha': 'yiU6hds3', 'nivel': 'usuario'},
                  {'usuario': 'Carlos', 'senha': 'QC59yFVo', 'nivel': 'usuario'},
                  {'usuario': 'Juliana', 'senha': 'uSi7REKw', 'nivel': 'usuario'}]

while True:
    system("cls")
    print("[1] - Adicionar usuário")
    print("[2] - Editar usuário")
    print("[3] - Encerrar")
    opcao = input("\nSelecione: ")

    if opcao == "1":
        system("cls")
        print("[Cadastro de Usuários]\n")

        cadastro = {
            "usuario": input("Informe o nome de usuário: "),
            "senha": input("Informe a senha: "),
            "nivel": input("Informe seu nível de acesso: ")
        }
        lista_usuarios.append(cadastro)

        print(f"\n*** {cadastro['usuario']} foi cadastrado com sucesso.")

        print("\n\nPressione qualquer tecla para continuar...")
        getch()

    if opcao == "2":
        pesquisa = input("\nInforme o usuário para editar: ")

        localizado = False
        for u in lista_usuarios:
            if pesquisa == u["usuario"]:
                localizado = True
                u["usuario"] = input("Insira seu novo usuário: ")
                print(f"\n{u['usuario']} editado com sucesso!")
                break

        if not localizado:
            print("\nUsuário não encontrado!")

        print("\n\nPressione qualquer tecla para continuar...")
        getch()

    if opcao == "3":
        system("cls")
        print("Saindo...")
        break
