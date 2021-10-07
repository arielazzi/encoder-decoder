import ErrorCorrectionCode
import codification.Fibonacci
import codification.Golomb
import codification.delta
import codification.elias_gamma
import codification.hamming
import codification.unaria
import utils


def menu1():
    print("[1] Codificar")
    print("[2] Decodificar")
    print("[3] Codidicar tratamento de erro")
    print("[4] Decodificar tratamento de erro")
    print("[0] Sair")


menu1()
operation = int(input("Escolha a operação: "))


def menu():
    print("[0] Golomb")
    print("[1] Elias-Gamma")
    print("[2] Fibonacci")
    print("[3] Unária")
    print("[4] Delta")


file = utils.load_file()
if operation == 1:
    menu()
    option = int(input("Escolha o método para realizar a codificação: "))
    output_file = open(file.name + '.cod', 'w+b')
    codification_type = bin(option)[2:].zfill(8)  # aqui pegamos a representação binaria do método (uma string)
    utils.write_text_in_file(output_file, codification_type)
    golomb_divider = ''

    text = file.read()
    encoded_text = ''
    if option == 0:
        golomb_selection = int(input("Divisor que será utilizado: "))
        golomb_divider = bin(golomb_selection)[2:].zfill(8)
        utils.write_text_in_file(output_file, golomb_divider)
        encoded_text = codification.Golomb.encode(text, output_file, golomb_selection)
        output_file.close()
    elif option == 1:
        golomb_divider = bin(0)[2:].zfill(8)
        utils.write_text_in_file(output_file, golomb_divider)
        codification.elias_gamma.encode(text, output_file)
        output_file.close()
    elif option == 2:
        golomb_divider = bin(0)[2:].zfill(8)
        utils.write_text_in_file(output_file, golomb_divider)
        codification.Fibonacci.encode(text, output_file)
        output_file.close()
    elif option == 3:
        golomb_divider = bin(0)[2:].zfill(8)
        utils.write_text_in_file(output_file, golomb_divider)
        codification.unaria.encode(text, output_file)
        output_file.close()
    elif option == 4:
        golomb_divider = bin(0)[2:].zfill(8)
        utils.write_text_in_file(output_file, golomb_divider)
        codification.delta.encode(text, output_file)
        output_file.close()
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

elif operation == 3:
    ErrorCorrectionCode.generateECC(file)

elif operation == 4:
    # TODO: Tem um bit perdido no calculo do CRC
    # TODO: Verificar se tem erro no CRC
    option = bin(int.from_bytes(file.read(1), 'big'))[2:].zfill(8)
    golomb_divider = bin(int.from_bytes(file.read(1), 'big'))[2:].zfill(8)
    crc = bin(int.from_bytes(file.read(1), 'big'))[2:].zfill(8)

    hamming = codification.hamming.decode(file)
    decodedText = str(option) + str(golomb_divider) + hamming
    utils.write_text_in_file(open(file.name.replace(".ecc",""), 'w+b'), decodedText, True)
    file.close()
    print("Informações de Hamming salvas no aquivo log.txt")
    print("Arquivo .cod final gerado")

    ErrorCorrectionCode.verificaCRC(crc, open(file.name.replace(".ecc",""), 'rb'))


print("Fim")
