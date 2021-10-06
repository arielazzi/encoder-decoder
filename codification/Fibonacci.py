import math
import utils

from os import environ
def encode(fileContent, output_file):

    stopBit = 1
    encodedText = ""
    encodedChar = ""
    seqFibonacci = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]
    soma = 0
    codification_type = "00000010"  # Fibonacci
    golomb_divider = "00000000"  # Used only in Golomb encoding

    # fileContent = file.read()
    rest = ''
    for i, letter in enumerate(range(0, len(fileContent))):

        asciiCharValue = fileContent[letter]
        print("Letra: "+ str(asciiCharValue))
        soma = asciiCharValue

        for numFibonacci in reversed(seqFibonacci):
            if(asciiCharValue >= numFibonacci):
                if((soma - numFibonacci) >= 0):
                    encodedChar += "1"
                    soma -= numFibonacci
                else:
                    encodedChar += "0"

        encodedText = encodedChar[::-1] + str(stopBit)
        rest = utils.write_text_in_file(output_file, rest + encodedText, (i + 1) == len(fileContent))
        print(encodedChar[::-1])
        encodedChar = ""
    # print("Codificação salva no arquivo: " + file.name + '.cod')

    # utils.write_file_in_bytes(codification_type + golomb_divider + encodedText, file.name)

def decode(file):

    decodedText = ""
    encodedChar = ""
    seqFibonacci = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]
    anterior = 0
    soma = 0
    indice = 0

    fileContent =  utils.binary_file_to_string(file)

    for letter in range(0, len(fileContent)):

        asciiCharValue = ord(fileContent[letter])

        if(anterior == 49 & asciiCharValue == 49):
            decodedText += chr(soma)
            soma = 0
            indice = 0
            asciiCharValue = 0
        else:
            if(asciiCharValue == 49):
                soma += seqFibonacci[indice]
            indice += 1

        anterior = asciiCharValue

    new_file = open(file.name[:len(file.name) - 8] + '_decoded.txt', 'w', newline='')
    new_file.write(decodedText)
    print("Decodificação salva no arquivo: " + new_file.name)
    new_file.close()
        


    
