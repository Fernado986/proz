from os import system
system('cls')

try:
    salario = float(input("Informe seu salário: "))
    print(f"Você recebe R${salario / 30:.2f} por dia!")

except ValueError:
    print("Você deve informar um valor numérico!")