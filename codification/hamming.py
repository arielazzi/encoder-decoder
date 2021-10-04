import utils


def encode(file):
    option = int.from_bytes(file.read(1), 'big')
    golomb_divider = int.from_bytes(file.read(1), 'big')
    print(option)
    print(golomb_divider)

    new_file = open(file.name + '.something', 'w+b')
    file_content = utils.binary_file_to_string(file)
    i = 0
    while i < len(file_content):
        parity_bit = ''
        parity_bit += calc_parity_bit(file_content[i], file_content[i + 1], file_content[i + 2])
        parity_bit += calc_parity_bit(file_content[i + 1], file_content[i + 2], file_content[i + 3])
        parity_bit += calc_parity_bit(file_content[i], file_content[i + 2], file_content[i + 3])
        asd = file_content[i:i + 4] + parity_bit
        print(asd + '0')
        new_file.write(utils.int_to_bytes(asd + '0'))
        i += 4
    new_file.close()


def calc_parity_bit(a, b, c):
    if (int(a) + int(b) + int(c)) % 2 == 0:
        return '0'
    return '1'


def decode(file):
    file_content = utils.binary_file_to_string(file)
    i = 0
    print(file_content)
    while i < len(file_content):
        print(file_content[i])
        i += 1
