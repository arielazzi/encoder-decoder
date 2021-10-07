import math
import ErrorCorrectionCode
import utils

from os import environ
def encode(fileContent, output_file, divider):
    # divider = int(input("Divisor que será utilizado: "))

    stopBit = 1
    suffixSize = math.log(divider, 2)
    encodedText = ""
    rest = ''
    # fileContent = file.read()
    for i, letter in enumerate(range(0, len(fileContent))):
        
        asciiCharValue = fileContent[letter]
        #print(asciiCharValue)

        prefix = bin(0)[2:].zfill(asciiCharValue // divider) # n quantidade de zeros
        suffix = bin(asciiCharValue % divider)[2:].zfill(int(suffixSize)) # resto em biário com n dígitos

        encodedText = prefix + str(stopBit) + suffix
        rest = utils.write_text_in_file(output_file, rest + encodedText, (i + 1) == len(fileContent))
    
def decode(file, divider):
    #faz o tratamento de erross
    fileContent = utils.binary_file_to_string(file)
    prefixTotal = 0 # quantidade de 0 no prefixo
    suffixSize = int(math.log(divider, 2))
    letter = 0
    decoded_text = ''

    while letter < len(fileContent):
        prefixTotal += 1
        suffixCharValue = ''
        if fileContent[letter] == '1': #encontra stopBit
            i=1
            quotient = prefixTotal - 1 # remove 1 pois não contamos o stop bit
                        
            while i <= suffixSize:
                suffixCharValue += fileContent[letter+i] # guarda os valores depois do stop bit para obter o resto
                i+=1
            
            decoded_text += chr(divider * quotient + int(suffixCharValue, 2)) # calcula o dividendo, converte para char e armazena a letra
            prefixTotal = 0
            letter += suffixSize + 1
           
        else:
            letter+=1

    new_file = open(file.name[:len(file.name) - 8] + '_decoded.txt', 'w', newline='')
    new_file.write(decoded_text)
    print("Decodificação salva no arquivo: " + new_file.name)
    new_file.close()
