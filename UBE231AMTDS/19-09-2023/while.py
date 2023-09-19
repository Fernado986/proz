# append()  -   Adiciona elementos a uma lista
# len()     -   Retorna a quantidade de elementos em uma lista
# sum()     -   Realiza uma soma de todos os valores dentro da lista

# Ajuste o código para que o programa encerre apenas quando o usuário digitar -1. Caso o usuário
# digite uma nota fora do intervalo entre 0 e 10, escreva a mensagem: entrada inválida!

notas = []
while True:
    nota = float(input("Digite uma nota: "))

    if nota >= 0 and nota <= 10:
        notas.append(nota)
    elif nota == -1:
        break
    else:
        print("Entrada Inválida!")

    print(notas)

media = sum(notas) / len(notas)
print(media)
