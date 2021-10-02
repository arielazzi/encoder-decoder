import utils


def encode(file):
    new_file = open(file.name + '.cod', 'w+b')
    codification_type = "00000011"  # Unaria
    golomb_divider = "00000000"  # Used only in Golomb encoding
    new_file.write(utils.int_to_bytes(codification_type))
    new_file.write(utils.int_to_bytes(golomb_divider))

    file_content = file.read()
    stop_bit = 1
    encoded_text = ""
    rest = ""
    for i, letter in enumerate(range(0, len(file_content))):
        ascii_char = file_content[letter]
        encoded_text += bin(0)[2:].zfill(ascii_char) + str(stop_bit)
        rest = utils.write_text_in_file(new_file, rest + bin(0)[2:].zfill(ascii_char) + str(stop_bit),
                                        (i + 1) == len(file_content))

    new_file.close()
    print("Codificação salva no arquivo: " + file.name + '.cod')


def decode(file):
    file_content = utils.binary_file_to_string(file)
    decoded_text = ""
    total = 0
    for letter in range(0, len(file_content)):

        if file_content[letter] == '0':
            total += 1
        else:
            if file_content[letter + 1] == '1':
                break
            decoded_text = decoded_text + chr(total)
            total = 0

    decoded_text = decoded_text + chr(total)

    new_file = open(file.name[:len(file.name) - 8] + '_decoded.txt', 'w+')
    new_file.writelines(decoded_text)
    print("Decodificaçâo salva no arquivo: " + new_file.name)
    new_file.close()
