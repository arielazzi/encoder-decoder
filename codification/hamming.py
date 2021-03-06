from datetime import datetime

import utils

def encode(file):
    option = int.from_bytes(file.read(1), 'big')
    golomb_divider = int.from_bytes(file.read(1), 'big')

    encoded_text = ""
    file_content = utils.binary_file_to_string(file)
    i = 0
    while i < len(file_content):
        parity_bit = ''
        parity_bit += calc_parity_bit(file_content[i], file_content[i + 1], file_content[i + 2])
        parity_bit += calc_parity_bit(file_content[i + 1], file_content[i + 2], file_content[i + 3])
        parity_bit += calc_parity_bit(file_content[i], file_content[i + 2], file_content[i + 3])
        encoded_text += file_content[i:i + 4] + parity_bit + '0'
        i += 4
    return encoded_text


def calc_parity_bit(a, b, c):
    if (int(a) + int(b) + int(c)) % 2 == 0:
        return '0'
    return '1'


def decode(file):
    log = open('log.txt', 'w+')
    file_content = utils.binary_file_to_string(file)
    i = 0
    print(file_content)
    output = ''
    while i < len(file_content):
        print('i', i)
        op5 = calc_parity_bit(file_content[i], file_content[i + 1], file_content[i + 2]) == file_content[i + 4]
        op6 = calc_parity_bit(file_content[i + 1], file_content[i + 2], file_content[i + 3]) == file_content[i + 5]
        op7 = calc_parity_bit(file_content[i], file_content[i + 2], file_content[i + 3]) == file_content[i + 6]

        if not op5 and op6 and op7:  # Error only on top
            log.writelines('[' + str(datetime.now()) + ']' + ' O primeiro bit de paridade está errado\n')
            output += file_content[i] + file_content[i + 1] + file_content[i + 2] + file_content[i + 3]
        else:
            output += file_content[i:i + 4]
            i += 8
            continue

        if not op5 and not op6 and op7:  # Error on top and right
            log.writelines('[' + str(datetime.now()) + ']' + ' O primeiro e o segundo bit de paridade estão com erro\n')
            output += file_content[i] + ('1' if file_content[i + 1] == '0' else '0') + file_content[i + 2] + file_content[i + 3]
        else:
            output += file_content[i:i + 4]
            i += 8
            continue

        if not op5 and not op7 and op6:  # Error on top and left
            log.writelines('[' + str(datetime.now()) + ']' + ' O primeiro e o terceiro bit de paridade estão com erro\n')
            output += ('1' if file_content[i] == '0' else '0') + file_content[i + 1] + file_content[i + 2] + file_content[i + 3]
        else:
            output += file_content[i:i + 4]
            i += 8
            continue

        if not op5 and not op6 and not op7:  # Error on top, left and right
            log.writelines('[' + str(datetime.now()) + ']' + ' O primeiro, o segundo e o terceiro bit de paridade estão com erro\n')
            output += file_content[i] + file_content[i + 1] + ('1' if file_content[i + 2] == '0' else '0') + file_content[i + 4]
        else:
            output += file_content[i:i + 4]
            i += 8
            continue

        if not op6 and op5 and op7:  # Error on left
            log.writelines('[' + str(datetime.now()) + ']' + ' O segundo bit de paridade está com erro\n')
            output += file_content[i] + file_content[i + 1] + file_content[i + 2] + file_content[i + 3]
        else:
            output += file_content[i:i + 4]
            i += 8
            continue

        if not op6 and not op7 and op5:  # Error on left and right
            log.writelines('[' + str(datetime.now()) + ']' + ' O segundo e o terceiro bit de paridade estão com erro\n')
            output += file_content[i] + file_content[i + 1] + file_content[i + 2] + ('1' if file_content[i + 3] == '0' else '0')
        else:
            output += file_content[i:i + 4]
            i += 8
            continue

        if not op7 and op5 and op6:  # Error on right
            log.writelines('[' + str(datetime.now()) + ']' + ' O terceiro bit de paridade está errado\n')
            output += file_content[i] + file_content[i + 1] + file_content[i + 2] + file_content[i + 3]
        else:
            output += file_content[i:i + 4]
            i += 8
            continue

        i += 8
    return output