import math


def encode(file):
    file_content = file.read()
    stop_bit = 1
    encoded_text = ""
    print(file_content)
    for letter in range(0, len(file_content)):
        ascii_char = ord(file_content[letter])
        higher_pow = int(math.log(ascii_char, 2))
        prefix = bin(0)[2:].zfill(higher_pow)
        suffix = bin(higher_pow)[2:].zfill(int(higher_pow))
        encoded_text += prefix + str(stop_bit) + suffix

    new_file = open(file.name + '.cod', 'w+')
    new_file.writelines(str(10) + encoded_text)
    print("Codificaçâo salva no arquivo: " + new_file.name)
    new_file.close()
