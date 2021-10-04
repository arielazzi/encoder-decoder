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

    inferior_limit = 0
    upper_limit = 8
    
    max_limit = len(file_content)

    last_character_as_chr = ""

    while upper_limit <= max_limit:
        current_character_to_decode = file_content[inferior_limit:upper_limit]

        inferior_limit = upper_limit
        upper_limit += 8

        current_character_as_int = int(current_character_to_decode, 2)

        if current_character_as_int != 0 and current_character_as_int != 1:
            current_character_as_chr = chr(current_character_as_int)
            decoded_text += current_character_as_chr 
            last_character_as_chr = current_character_as_chr

        elif current_character_as_int == 0:
            decoded_text += last_character_as_chr
    
    new_file = open(file.name[:len(file.name) - 8] + '_decoded.txt', 'w', newline='')
    new_file.write(decoded_text)
    print("Decodificação salva no arquivo: " + new_file.name)
    new_file.close()