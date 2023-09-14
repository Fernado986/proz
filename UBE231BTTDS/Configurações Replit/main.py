import os


def clear_console():
    os.system('clear')

files = [f for f in os.listdir() if f.endswith('.py') and f != 'main.py']

for i, f in enumerate(files):
    print(f"{i + 1}. {f}")

choice = int(input("Escolha o número do arquivo para executar: ")) - 1

if 0 <= choice < len(files):
    clear_console()
    os.system(f"python3 {files[choice]}")
else:
    print("Escolha inválida!")
