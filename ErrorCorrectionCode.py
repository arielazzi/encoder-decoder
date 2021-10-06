import codification.hamming
import utils 

def generateECC(file):
    # fileContent = file.read()
    fileContent = utils.binary_file_to_string(file)

    # calcular o CRC
    decimalFirstBitCRC = int(fileContent[0:8], 2) #Transforma string binaria em decimal ex.: "00000011" -> 3
    decimalSecondBitCRC = int(fileContent[8:16], 2)

    hexResultCRC = calculateCRC(decimalFirstBitCRC, decimalSecondBitCRC)
    byteResultCRC = bin(int(hexResultCRC, 16))[2:].zfill(8)
    encodedText = bin(decimalFirstBitCRC)[2:].zfill(8) + bin(decimalSecondBitCRC)[2:].zfill(8) + byteResultCRC

    # encode hamming
    hammingBits = codification.hamming.encode(open(file.name, 'rb'))
    encodedText += hammingBits 
    
    # gera arquivo.ecc
    #print(encodedText)
    utils.write_file_in_bytes_ecc(encodedText, file.name)
    print("Gerado o arquivo .ecc... ")

    
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

def verificaCRC(CRC, file):
    # fileContent = file.read()
    fileContent = utils.binary_file_to_string(file)

    # calcular o CRC
    decimalFirstBitCRC = int(fileContent[0:8], 2) #Transforma string binaria em decimal ex.: "00000011" -> 3
    decimalSecondBitCRC = int(fileContent[8:16], 2)    

    hexResultCRC = calculateCRC(decimalFirstBitCRC, decimalSecondBitCRC)

    if (hex(int(CRC, 2)).split('x')[-1] != hexResultCRC):
        print("Valores diferentes para CRC... decodificação não é recomendada")
