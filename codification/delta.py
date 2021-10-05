import utils

def encode(file):
    file_content = file.read()

    encoded_text = ""
    current_character = ""
    last_character = ""

    for i in range(0, len(file_content)):
        if current_character != file_content[i] and i == 0:
            character = bin(file_content[i])[2:].zfill(8)
        elif current_character != file_content[i]:
            current_character_as_bin = bin(file_content[i])
            last_character_as_bin = bin(last_character)

            difference = int(current_character_as_bin, 2) - int(last_character_as_bin, 2)

            if difference < 0:
                difference = abs(difference)

                difference_encoded = bin(1)[2:] + bin(difference)[2:].zfill(7) #signed to represent negative diff
                character = bin(1)[2:].zfill(8) + difference_encoded
            else:
                difference_encoded = bin(0)[2:] + bin(difference)[2:].zfill(7)
                character = bin(1)[2:].zfill(8) + difference_encoded
        else:
            character = bin(0)[2:].zfill(8)
        last_character = current_character
        current_character = file_content[i]
        encoded_text += character

    codification_type = "00000100"
    golomb_divider = "00000000"  # Used only in Golomb encoding
    utils.write_file_in_bytes(codification_type + golomb_divider + encoded_text, file.name)
    print("Codificação salva no arquivo: " + file.name + ".cod")

def decode(file):
    file_content = utils.binary_file_to_string(file)

    decoded_text = ""
    last_decoded_character = ""
    current_character_to_decode = ""
    calculating_change = False

    inferior_limit = 0
    upper_limit = 8

    max_limit = len(file_content)

    while upper_limit <= max_limit:
        current_character_to_decode = file_content[inferior_limit:upper_limit]
        current_character_as_int = int(current_character_to_decode)

        inferior_limit = upper_limit
        upper_limit += 8

        if calculating_change == True:
            is_diff_positive = current_character_to_decode[0] == 0

            last_character_as_int = int(last_decoded_character, 2)
            difference = int(current_character_to_decode[1:], 2)

            if is_diff_positive == True:
                next_to_decode = last_character_as_int + difference
            else:
                next_to_decode = last_character_as_int - difference

            next_to_decode_as_chr = chr(next_to_decode)
            decoded_text += next_to_decode_as_chr

            last_decoded_character = bin(next_to_decode)[2:].zfill(8)

            calculating_change = False

            continue

        if last_decoded_character == "":
            current_character_as_int = int(current_character_to_decode, 2)
            current_character_as_chr = chr(current_character_as_int)
            decoded_text += current_character_as_chr
            last_decoded_character = current_character_to_decode
            continue

        if current_character_as_int == 0:
            last_character_as_int = int(last_decoded_character, 2)
            last_character_as_chr = chr(last_character_as_int)
            decoded_text += last_character_as_chr
            continue
        
        if current_character_as_int == 1 and calculating_change != True:
            calculating_change = True
            continue
    
    new_file = open(file.name[:len(file.name) - 8] + '_decoded.txt', 'w', newline='')
    new_file.write(decoded_text)
    print("Decodificação salva no arquivo: " + new_file.name)
    new_file.close()