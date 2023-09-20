filmes = []

nr_filmes = int(input("Quantos filmes você quer adicionar? "))

for i in range(nr_filmes):
    filmes.append(input("Informe o nome do filme: "))

print("\n\n\n")

for i in range(len(filmes)):
    print(f"Filme {i+1}: {filmes[i]}")
