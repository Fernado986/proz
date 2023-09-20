receita = []

while True:
  ingrediente = input("Informe um ingrediente: ")

  if ingrediente == "Sair":
    break

  else:
    receita.append(ingrediente)

for i in range(len(receita)):
  print(f"- {receita[i]}")
