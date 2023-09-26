from os import system

if __name__ == "__main__":

    palavra_secreta = "banana"
    letras_erradas = []
    jogo = ["_", "_", "_", "_", "_", "_"]

    erros = 0
    while True:
        system("cls")
        print(f"Restam {6 - erros} tentativas!\n")
        print(jogo, "\n\n")
        print(f"Letras erradas: {letras_erradas}\n\n")
        chute = input("Informe a letra: ")

        # Verifica se a letra que o usuario chutou existe na palavra secreta
        if chute in palavra_secreta:
            indice = 0

            # Itera sobre a palavra secreta, onde cada loop representa uma letra
            for letra in palavra_secreta:
                if letra == chute:
                    jogo[indice] = letra  # Edita a lista jogo, substituindo o _ pela letra correta
                indice += 1
        else:
            erros += 1  # Caso a letra não exista dentro da palavra, ele adicionará +1 a variavel erros
            letras_erradas.append(chute)  # Adiciona a letra errada dentro de uma lista

        if erros == 6:
            print("Você foi enforcado!")
            break

        if "_" not in jogo:
            print("Parabéns, você acertou!")
            break


