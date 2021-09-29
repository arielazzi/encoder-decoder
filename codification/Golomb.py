import math

from os import environ
def encode(file):
    divider = int(input("Divisor que será utilizado: "))

    stopBit = 1
    suffixSize = math.log(divider, 2)
    encodedText = ""

    fileContent = file.read()
    for letter in range(0, len(fileContent)):
        
        asciiCharValue = fileContent[letter]
        #print(asciiCharValue)

        prefix = bin(0)[2:].zfill(asciiCharValue // divider) # n quantidade de zeros
        suffix = bin(asciiCharValue % divider)[2:].zfill(int(suffixSize)) # resto em biário com n dígitos

        encodedText += prefix + str(stopBit) + suffix

    newFile = open(file.name + '.cod', 'w+')
    newFile.writelines(str(0) + str(divider) + encodedText)
    print("Codificaçâo salva no arquivo: " + newFile.name)
    newFile.close()

def decode(file, divider):
    fileContent = file.read()
    prefixTotal = 0 # quantidade de 0 no prefixo
    divider = int(chr(divider))
    suffixSize = int(math.log(divider, 2))
    letter = 0
    decoded_text = ''

    while letter < len(fileContent):
        prefixTotal += 1
        suffixCharValue = ''
        if fileContent[letter] == 49: #encontra stopBit
            i=1
            quotient = prefixTotal - 1 # remove 1 pois não contamos o stop bit
                        
            while i <= suffixSize:
                suffixCharValue += chr(fileContent[letter+i]) # guarda os valores depois do stop bit para obter o resto
                i+=1
            
            decoded_text += chr(divider * quotient + int(suffixCharValue, 2)) # calcula o dividendo, converte para char e armazena a letra
            prefixTotal = 0
            letter += suffixSize + 1
           
        else:
            letter+=1

    new_file = open(file.name[:len(file.name) - 8] + '_decoded.txt', 'w', newline='')
    new_file.write(decoded_text)
    print("Decodificaçâo salva no arquivo: " + new_file.name)
    new_file.close()
