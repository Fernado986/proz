from time import sleep
from os import system

segundos = int(input("Informe o tempo em segundos: "))

while True:
    segundos -= 1
    if segundos < 0:
        break
    
    print(segundos)
    sleep(1)
    system("cls")


    