import utils

def encode(file):
    file_content = file.read()

    encoded_text = ''
    current_character = ''

    for i in range(0, len(file_content)):
        character = format(file_content[i], "b") if current_character != file_content[i] else format(0, "b")
        print(character)
        current_character = file_content[i]
        encoded_text += character

    codification_type = "00000101"
    golomb_divider = "00000000"  # Used only in Golomb encoding
    utils.write_file_in_bytes(codification_type + golomb_divider + encoded_text, file.name)
    print("Codificação salva no arquivo: " + file.name + '.cod')

def decode(file):
    print("Decodificação Delta")