"""
Este código é um simples jogo de adivinhação. Ele seleciona aleatoriamente um número entre 1 e 10, 
e em seguida, permite ao usuário fazer três tentativas para adivinhar o número.
A cada tentativa, o código verifica se o chute do usuário está correto:

Se estiver correto, exibe uma mensagem de felicitação ("Parabéns, você acertou!") e encerra o jogo.

Se estiver errado, informa ao usuário para tentar novamente e fornece mais uma chance para adivinhar.

Após o usuário ter feito três tentativas ou adivinhado o número corretamente, o programa revela qual era o número correto.
"""

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
