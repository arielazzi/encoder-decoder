def load_file():
    try:
        file = open(input("Caminho do arquivo: "), 'rb')
    except FileNotFoundError:
        print("Arquivo não existe, digite um caminho válido! ")
    return file


# encoded_text = Algo tipo 000100100101
def write_file_in_bytes(encoded_text, file_name):
    new_file = open(file_name + '.cod', 'w+b')
    while len(encoded_text) >= 8:
        new_file.write(int_to_bytes(encoded_text))
        encoded_text = encoded_text[8:]

    if 0 < len(encoded_text) < 8:
        new_file.write(int_to_bytes(encoded_text.ljust(8, '0')))

    new_file.close()


def int_to_bytes(number: int) -> bytes:
    return bytes([int(number[:8], 2)])


def binary_file_to_string(binary_file):
    binary_text = ''
    binary = binary_file.read(1)
    while binary != b'':
        binary_text += bin(int.from_bytes(binary, 'big'))[2:].zfill(8)
        binary = binary_file.read(1)
    return binary_text
