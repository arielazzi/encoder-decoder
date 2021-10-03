import utils

def encode(file):
    file_content = file.read()

    encoded_text = ''
    current_character = ''

    for i in range(0, len(file_content)):
        if current_character != file_content[i] and i == 0:
            character = format(file_content[i], "b") 
        elif current_character != file_content[i]:
            character = format(1, "b") + format(file_content[i], "b") 
        else:
            character = format(0, "b")
        current_character = file_content[i]
        encoded_text += character

    codification_type = "00000101"
    golomb_divider = "00000000"  # Used only in Golomb encoding
    utils.write_file_in_bytes(codification_type + golomb_divider + encoded_text, file.name)
    print("Codificação salva no arquivo: " + file.name + '.cod')

def decode(file):
    print("Decodificação Delta")