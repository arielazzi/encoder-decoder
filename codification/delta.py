def encode(file):
    file_content = file.read()

    encoded_text = ''
    current_character = ''

    for i in range(0, len(file_content)):
        character = bin(file_content[i]) if current_character != file_content[i] else bin(0)
        current_character = file_content[i]
        encoded_text += character

    new_file = open(file.name + '.cod', 'w+')
    new_file.writelines(str(50) + encoded_text)
    print('Codificação salva no arquivo: ' + new_file.name)
    new_file.close()

def decode(file):
    print("Decodificação Delta")