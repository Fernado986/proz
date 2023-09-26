def jogar():
    print("*********************************")
    print("** Bem vindo ao jogo da Forca! **")
    print("*********************************")

    palavra_secreta = "banana"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False
    erros = 0

    for item in letras_acertadas:
        print(item, end=" ")

    # enquanto não enforcou e não acertou
    while not enforcou and not acertou:
        chute = input("\n\nQual letra? ")

        index = 0
        if chute in palavra_secreta:
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        enforcou = erros == 6

        for item in letras_acertadas:
            print(item, end=" ")

    print("Fim do jogo")


if __name__ == "__main__":
    jogar()
