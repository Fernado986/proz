import random

numero = random.randint(1, 10)

for i in range(3):
  jogada = int(input("Chute um número: "))

  if jogada == numero:
    print("Parabens, você acertou!")
    break
    
  else:
    print("Tente novamente!\n")

print(f"\nO número é: {numero}")
