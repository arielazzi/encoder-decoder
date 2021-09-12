import math

from os import environ
def encode(file):

    stopBit = 1
    encodedText = ""
    encodedChar = ""
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
                    encodedChar += "1"
                    soma -= numFibonacci
                else:
                    encodedChar += "0"

        encodedText += encodedChar[::-1] + str(stopBit)
        print(encodedChar[::-1])
        encodedChar = ""

    newFile = open(file.name + '.cod', 'w+')
    newFile.writelines(str(2) + str(0) + encodedText)
    newFile.close()

def decode(file):

    encodedText = ""
    encodedChar = ""
    seqFibonacci = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]
    anterior = 0
    soma = 0
    indice = 0

    fileContent = file.read()

    print(fileContent)
    for letter in range(0, len(fileContent)):

        asciiCharValue = ord(fileContent[letter])

        print(asciiCharValue)

        if(anterior == 49 & asciiCharValue == 49):
            encodedText += chr(soma)
            soma = 0
            indice = 0
            asciiCharValue = 0
        else:
            if(asciiCharValue == 49):
                soma += seqFibonacci[indice]
            indice += 1

        anterior = asciiCharValue
    print(encodedText)

    newFile = open(file.name + '.txt', 'w+')
    newFile.writelines(encodedText)
    newFile.close()
        


    
