# Inicializa uma lista vazia chamada frutas.
frutas = []

print("Bem-vindo ao programa de registro de frutas!")
print("Digite o nome das frutas que deseja adicionar à lista.")
print("Quando terminar, simplesmente digite 'Sair'.\n")

# Inicia um loop infinito.
while True:
  # Solicita ao usuário que insira o nome de uma fruta ou digite "Sair".
  comando = input("Insira uma fruta, ou digite Sair: ")

  # Se o usuário digitar "Sair", o loop é interrompido.
  if comando == "Sair":
    break
  # Se qualquer outra coisa for inserida, essa coisa (neste contexto, uma fruta) é adicionada à lista de frutas.
  else:
    frutas.append(comando)

print("\nAqui está a lista de frutas que você inseriu:")

# Após a interrupção do loop, o programa percorre cada item na lista de frutas e imprime na tela
for fruta in frutas:
  print(f"{fruta}")
