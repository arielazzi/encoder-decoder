import utils

def encode(file):
    file_content = file.read()

    codification_type = '00000101'
    golomb_divider = '00000000'

    encoded_text = ''

    for i in range(0, len(file_content)):
        print(file_content[i])
        print(bin(file_content[i]))
        encoded_text += bin(file_content[i])

    utils.write_file_in_bytes(codification_type + golomb_divider + encoded_text, file.name)

def decode(file):
    print('Decode Delta')