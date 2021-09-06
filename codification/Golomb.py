import math

from os import environ
def encode():
    divider = int(input("Divisor que será utilizado: "))
    try:
        file = open(input("Caminho do arquivo: "), 'r')
    except FileNotFoundError:
        print("Arquivo não existe, digite um caminho válido! ")

    stopBit = 1
    sufixoSize = math.log(divider, 2)
    encodedText = ""

    fileContent = file.read()
    for letter in range(0, len(fileContent)):
        #print(fileContent[letter])

        asciiCharValue = ord(fileContent[letter])
        #print(asciiCharValue)

        prefixo = bin(0)[2:].zfill(asciiCharValue // divider) # n quantidade de zeros
        sufixo = bin(asciiCharValue % divider)[2:].zfill(int(sufixoSize)) # resto em biário com n dígitos
        #print("prefixo: "+prefixo)
        #print("stop bit: "+str(stopBit))
        #print("sufixo: "+sufixo)

        encodedText += prefixo + str(stopBit) + sufixo

    newFile = open(file.name + '.cod', 'w+')
    newFile.writelines(str(0) + str(divider) + encodedText)    
    print("Codificaçâo salva no arquivo: " + newFile.name)
    newFile.close()

        


    
