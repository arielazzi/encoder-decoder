def encode(file):
    file_content = file.read()
    stop_bit = 1
    encoded_text = ""
    for letter in range(0, len(file_content)):
        ascii_char = file_content[letter]
        encoded_text += bin(0)[2:].zfill(ascii_char) + str(stop_bit)

    new_file = open(file.name + '.cod', 'w+')
    new_file.writelines(str(30) + encoded_text[:-1])
    print("Codificaçâo salva no arquivo: " + new_file.name)
    new_file.close()


def decode(file):
    file_content = file.read()
    decoded_text = ""
    total = 0
    for letter in range(0, len(file_content)):
        print(file_content[letter])
        if file_content[letter] == 48:
            total += 1
        else:
            print(total)
            decoded_text = decoded_text + chr(total)
            total = 0
    decoded_text = decoded_text + chr(total)
    print(decoded_text)

    new_file = open(file.name[:len(file.name) - 8] + '_decoded.txt', 'w+')
    new_file.writelines(decoded_text)
    print("Decodificaçâo salva no arquivo: " + new_file.name)
    new_file.close()
