def load_file():
    try:
        file = open(input("Caminho do arquivo: "), 'rb')
    except FileNotFoundError:
        print("Arquivo não existe, digite um caminho válido! ")
    return file
