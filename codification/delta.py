import utils

def encode(file):
    file_content = file.read()

    encoded_text = ""
    current_character = ""

    for i in range(0, len(file_content)):
        if current_character != file_content[i] and i == 0:
            character = bin(file_content[i])[2:].zfill(8)
        elif current_character != file_content[i]:
            character = bin(1)[2:].zfill(8) + bin(file_content[i])[2:].zfill(8)
        else:
            character = bin(0)[2:].zfill(8)
        current_character = file_content[i]
        encoded_text += character

    codification_type = "00000100"
    golomb_divider = "00000000"  # Used only in Golomb encoding
    utils.write_file_in_bytes(codification_type + golomb_divider + encoded_text, file.name)
    print("Codificação salva no arquivo: " + file.name + ".cod")

def decode(file):
    file_content = utils.binary_file_to_string(file)

    decoded_text = ""
    current_character_to_decode = ""
    counter = 0

    for i in range(0, len(file_content)):
        if counter < 8:
            current_character_to_decode += file_content[i]
            counter += 1
        else:
            print(current_character_to_decode)
            current_character_to_decode = ""
            counter = 0