import codification.Fibonacci
import codification.Golomb
import codification.elias_gamma
import codification.unaria
import codification.delta

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
        codification.Golomb.encode(file)
    elif option == 2:
        codification.elias_gamma.encode(file)
    elif option == 3:
        codification.Fibonacci.encode(file)
    elif option == 4:
        codification.unaria.encode(file)
    elif option == 5:
        codification.delta.encode(file)
    else:
        option = int(input("Por favor, digite um método válido! "))
elif operation == 2:
    option = int.from_bytes(file.read(1), 'big')
    golomb_divider = int.from_bytes(file.read(1), 'big')
    if option == 0:
        codification.Golomb.decode(file, golomb_divider)
    elif option == 1:
        codification.elias_gamma.decode(file)
    elif option == 2:
        codification.Fibonacci.decode(file)
    elif option == 3:
        codification.unaria.decode(file)
    elif option == 4:
        codification.delta.decode(file)
    else:
        operation = int(input("Por favor, digite uma operação válida! "))

print("Fim")
