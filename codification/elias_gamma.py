import math

import utils


def encode(file_content, output_file):
    stop_bit = 1
    rest = ''
    for i, letter in enumerate(range(0, len(file_content))):
        ascii_char = file_content[letter] + 1
        higher_pow = int(math.log(ascii_char, 2))
        prefix = bin(0)[2:].zfill(higher_pow)
        suffix = bin(int(ascii_char - math.pow(2, higher_pow)))[2:].zfill(int(higher_pow))
        encoded_text = prefix + str(stop_bit) + suffix
        rest = utils.write_text_in_file(output_file, rest + encoded_text, (i + 1) == len(file_content))


def decode(file):
    file_content = utils.binary_file_to_string(file)
    decoded_text = ''
    total = 0
    i = 0
    while i < len(file_content):
        if file_content[i] == '0':
            total += 1
        else:
            ascii_char = int(math.pow(2, total)) + int(file_content[i + 1:i + 1 + total], 2) - 1
            decoded_text += chr(ascii_char)
            i = i + total
            total = 0
        i += 1

    new_file = open(file.name[:len(file.name) - 8] + '_decoded.txt', 'w', newline='')
    new_file.write(decoded_text)
    print("Decodificação salva no arquivo: " + new_file.name)
    new_file.close()
