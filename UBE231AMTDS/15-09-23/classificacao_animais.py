# Importa o módulo 'os'  para executar comandos no terminal.
import os

# Inicializa uma string vazia chamada 'animal'.
animal = ""

# Imprime opções para o usuário escolher entre 'Vertebrado' e 'Invertebrado'.
print("[1] - Vertebrado")
print("[2] - Invertebrado")
coluna = int(input("Selecione: "))
os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela do terminal.

# Se o usuário escolher 'Vertebrado' (opção 1).
if coluna == 1:
    # Imprime opções para o usuário escolher entre 'Ave' e 'Mamífero'.
    print("[1] - Ave")
    print("[2] - Mamífero")
    classe = int(input("Selecione: "))
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela do terminal.

    # Se o usuário escolher 'Ave' (opção 1).
    if classe == 1:
        # Imprime opções de dieta para aves.
        print("[1] - Carnívoro")
        print("[2] - Onívoro")
        dieta = int(input("Selecione: "))

        # Determina o tipo de ave com base na dieta escolhida.
        if dieta == 1:
            animal = "Águia"
        elif dieta == 2:
            animal = "Pomba"

    # Se o usuário escolher 'Mamífero' (opção 2).
    elif classe == 2:
        # Imprime opções de dieta para mamíferos.
        print("[1] - Onívoro")
        print("[2] - Herbívoro")
        dieta = int(input("Selecione: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela do terminal.

        # Determina o tipo de mamífero com base na dieta escolhida.
        if dieta == 1:
            animal = "Homem"
        elif dieta == 2:
            animal = "Vaca"

# Se o usuário escolher 'Invertebrado' (opção 2).
elif coluna == 2:
    # Imprime opções para o usuário escolher entre 'Inseto' e 'Anelídeo'.
    print("[1] - Inseto")
    print("[2] - Anelídeo")
    classe = int(input("Selecione: "))
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela do terminal.

    # Se o usuário escolher 'Inseto' (opção 1).
    if classe == 1:
        # Imprime opções de dieta para insetos.
        print("[1] - Hematófago")
        print("[2] - Herbívoro")
        dieta = int(input("Selecione: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela do terminal.

        # Determina o tipo de inseto com base na dieta escolhida.
        if dieta == 1:
            animal = "Pulga"
        elif dieta == 2:
            animal = "Lagarta"

    # Se o usuário escolher 'Anelídeo' (opção 2).
    elif classe == 2:
        # Imprime opções de dieta para anelídeos.
        print("[1] - Hematófago")
        print("[2] - Onívoro")
        dieta = int(input("Selecione: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela do terminal.

        # Determina o tipo de anelídeo com base na dieta escolhida.
        if dieta == 1:
            animal = "Sanguessuga"
        elif dieta == 2:
            animal = "Minhoca"

# Imprime o tipo de animal determinado ou uma mensagem de erro se nenhuma seleção válida foi feita.
if animal != "":
    print(f"O tipo é: {animal}")
else:
    print("Entrada inválida!")
