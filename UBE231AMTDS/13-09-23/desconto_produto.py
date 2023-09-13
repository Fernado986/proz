'''
Você é um desenvolvedor e foi encarregado de criar um programa que aplica descontos a produtos de uma loja online. 
A loja tem as seguintes regras de desconto:

Se o produto custa mais do que R$100, ele tem um desconto de 10%.
Se o produto custa entre R$50 e R$100, ele tem um desconto de 5%.
Se o produto custa menos do que R$50, não há desconto.

Entrada: R$150
Saída esperada:
Preço original: R$150.00
Desconto: R$15.00
Preço com desconto: R$135.00

Entrada: R$70
Saída esperada:
Preço original: R$70.00
Desconto: R$3.50
Preço com desconto: R$66.50

Entrada: R$50
Saída esperada:
Preço original: R$50.00
Desconto: R$2.50
Preço com desconto: R$47.50
'''

valor = float(input("Insira o valor do produto: "))

desconto = 0

if valor > 100:
  desconto = 0.10

elif valor >= 50:
  desconto = 0.05

valor_desconto = valor * desconto
valor_com_desconto = valor - valor_desconto

print(f"Preço Original: R${valor:.2f}")
print(f"Desconto: {valor_desconto:.2f}")
print(f"Preço com desconto: R${valor_com_desconto:.2f}")
