notas = []

while True:
    nota = float(input("Informe sua nota: "))

    if nota < 0:
        break

    else:
        notas.append(nota)


print(notas)