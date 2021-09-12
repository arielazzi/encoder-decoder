import codification.Golomb
import codification.elias_gama
import codification.unaria
import codification.Fibonacci

import utils


def menu1():
    print("[1] Codificar")
    print("[2] Decodificar")
    print("[0] Sair")


menu1()
operation = int(input("Escolha a operação: "))


def menu():
    print("[1] Golomb")
    print("[2] Elias-Gamma")
    print("[3] Fibonacci")
    print("[4] Unária")
    print("[5] Delta")
    print("[0] Sair")


file = utils.load_file()
if operation == 1:
    menu()
    option = int(input("Escolha o método para realizar a codificação: "))
    if option == 1:
        codification.Golomb.encode()
    elif option == 2:
        codification.elias_gama.encode(file)
    elif option == 3:
        codification.Fibonacci.encode()
    elif option == 4:
        codification.unaria.encode(file)
    elif option == 5:
        print("5")
    else:
        option = int(input("Por favor, digite um método válido! "))
elif operation == 2:
    file_content = file.read()
    option = int(file_content[0])
    file.seek(2)
    if option == 0:
        print("decode Golomb")
    elif option == 1:
        print("decode Elias-Gama")
    elif option == 2:
        print("decode Fibonacci")
    elif option == 3:
        codification.unaria.decode(file)
    elif option == 4:
        print("decode Delta")
    else:
        operation = int(input("Por favor, digite uma operação válida! "))

print("Fim")
