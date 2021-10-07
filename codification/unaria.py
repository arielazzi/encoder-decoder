import utils


def encode(file_content, output_file):
    stop_bit = 1
    rest = ""
    for i, letter in enumerate(range(0, len(file_content))):
        ascii_char = file_content[letter]
        encoded_text = bin(0)[2:].zfill(ascii_char) + str(stop_bit)
        rest = utils.write_text_in_file(output_file, rest + encoded_text, (i + 1) == len(file_content))

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
