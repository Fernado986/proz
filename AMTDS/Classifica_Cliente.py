categoria = ""
nome = input("Informe seu nome: ")
valor = float(input("Informe o valor total de compras do último ano: "))

if valor <= 1000:
    categoria = "BRONZE"
elif valor <= 5000:
    categoria = "PRATA"
elif valor <= 10000:
    categoria = "OURO"
elif valor > 10000:
    categoria = "DIAMANTE"

print(f"{nome}, sua categoria é: {categoria}")

