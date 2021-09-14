import math


# Está faltanto implementar o uso do 0
def encode(file):
    file_content = file.read()
    stop_bit = 1
    encoded_text = ""

    for letter in range(0, len(file_content)):
        ascii_char = ord(file_content[letter])
        higher_pow = int(math.log(ascii_char, 2))
        prefix = bin(0)[2:].zfill(higher_pow)
        suffix = bin(int(ascii_char - math.pow(2, higher_pow)))[2:].zfill(int(higher_pow))
        encoded_text += prefix + str(stop_bit) + suffix

    new_file = open(file.name + '.cod', 'w+')
    new_file.writelines(str(10) + encoded_text)
    print("Codificaçâo salva no arquivo: " + new_file.name)
    new_file.close()


def decode(file):
    file_content = file.read()
    decoded_text = ''
    total = 0
    i = 0

    while i < len(file_content):
        if file_content[i] == '0':
            total += 1
        else:
            ascii_char = int(math.pow(2, total)) + int(file_content[i + 1:i + 1 + total], 2)
            decoded_text += chr(ascii_char)
            i = i + total
            total = 0
        i += 1

    new_file = open(file.name[:len(file.name) - 8] + '_decoded.txt', 'w+')
    new_file.writelines(decoded_text)
    print("Decodificaçâo salva no arquivo: " + new_file.name)
    new_file.close()
