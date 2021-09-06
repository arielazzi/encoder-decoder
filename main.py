import codification.Golomb

def menu():
    print("[1] Golomb")
    print("[2] Elias-Gamma")
    print("[3] Fibonacci")
    print("[4] Unária")
    print("[5] Delta")
    print("[0] Sair")

menu()
option = int(input("Escolha o método para realizar a codificação: "))

while option != 0:
    if option == 1:
        codification.Golomb.encode()
    elif option == 2:
        print("2")
    elif option == 3:
        print("3")
    elif option == 4:
        print("4")
    elif option == 5:
        print("5")
    else:
        option = int(input("Por favor, digite um método válido! "))
    
    print()
    menu()
    option = int(input("Escolha o método para realizar a codificação: "))

print("Fim")