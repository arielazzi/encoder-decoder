def generateECC(file):
    fileContent = file.read()
    decimalFirstBitCRC = int(fileContent[0])
    decimalSecondBitCRC = int(fileContent[1])

    hexResultCRC = calculateCRC(decimalFirstBitCRC, decimalSecondBitCRC)
    byteResultCRC = bin(int(hexResultCRC, 16))[2:].zfill(8)
    encodedText = str(decimalFirstBitCRC) + str(decimalSecondBitCRC) + str(byteResultCRC)
    
    #implementar o hamming aqui?
    for letter in range(2, len(fileContent)):
        encodedText += fileContent[letter]
    
def calculateCRC(firstBit, secondBit):
    CRCdivider = "100000111"

    binFirstBitCRC = bin(firstBit)[2:].zfill(8)
    binSecondBitCRC = bin(secondBit)[2:].zfill(8)
    CRCdividend = binFirstBitCRC + binSecondBitCRC + bin(0)[2:].zfill(8)
    CRCdividend = removeZeros(CRCdividend)
    stop = False
    result = CRCdividend

    while (not(stop)):
        if(len(CRCdividend) <= len(CRCdivider)):
            stop = True
        else:
            byteFinal = ""
            for bit in range(0, len(CRCdivider)):
                byteFinal += str(int(CRCdivider[bit]) ^ int(result[bit]))
            #remove zeros da esquerda
            byteFinal = removeZeros(byteFinal)
            #adiciona zeros restantes no byteFinal
            dif = len(CRCdivider) - len(byteFinal) 
            dif = len(CRCdividend) - len(CRCdivider) < dif and len(CRCdividend) - len(CRCdivider) or dif
            i = 0
            while (i < dif):
                byteFinal += '0'
                CRCdividend = CRCdividend[:-1:] #remove os zeros da direita
                i+=1
            result = byteFinal
    
    return hex(int(result, 2)).split('x')[-1]


def removeZeros(CRCdividend):
    stringAux = CRCdividend
    for i in range(0, len(CRCdividend)):
        if (CRCdividend[i] == '0'):
            stringAux = stringAux[1 : : ]
        else:
            break
    return stringAux