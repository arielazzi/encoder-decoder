import math

from os import environ
def encode():
    try:
        file = open(input("Caminho do arquivo: "), 'r')
    except FileNotFoundError:
        print("Arquivo não existe, digite um caminho válido! ")

    stopBit = 1
    encodedText = ""
    encodeChar = ""
    seqFibonacci = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]
    soma = 0

    fileContent = file.read()
    for letter in range(0, len(fileContent)):

        asciiCharValue = ord(fileContent[letter])
        print("Letra: "+str(asciiCharValue))
        soma = asciiCharValue

        for numFibonacci in reversed(seqFibonacci):
            if(asciiCharValue >= numFibonacci):
                if((soma - numFibonacci) >= 0):
                    encodeChar += "1"
                    soma -= numFibonacci
                else:
                    encodeChar += "0"

        encodedText += encodeChar[::-1] + str(stopBit)
        print(encodeChar[::-1])
        encodeChar = ""

    newFile = open(file.name + '.cod', 'w+')
    newFile.writelines(str(2) + str(0) + encodedText)
    newFile.close()

        


    
