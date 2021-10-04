def generateECC(file):
    fileContent = file.read()
    decimalFirstBitCRC = int(fileContent[0])
    decimalSecondBitCRC = int(fileContent[1])

    hexResultCRC = calculateCRC(decimalFirstBitCRC, decimalSecondBitCRC)

    #hamming
    #adicionar em arquivo ecc
    #salvar arquivo ecc
    #decodificar arquivo
    #verificar se existe algum erro
    #se houver erro, não permitir a decodificação do .cod ?
    for letter in range(2, len(fileContent)):
        print(fileContent[letter])
    
def calculateCRC(firstBit, secondBit):
    CRCdivider = "100000111"

    hexFirstBitCRC = hex(firstBit).split('x')[-1]
    hexSecondBitCRC = hex(secondBit).split('x')[-1]

    binFirstBitCRC = bin(int(hexFirstBitCRC, 16))[2:].zfill(8)
    binSecondBitCRC = bin(int(hexSecondBitCRC, 16))[2:].zfill(8)

    CRCdividend = str(binFirstBitCRC) + str(binSecondBitCRC)
    CRCdividend = removeZeros(CRCdividend)
    stop = False
    byteFinal = ""

    while (not(stop)):
        for bit in CRCdivider:
            byteFinal += str(int(CRCdivider[bit]) ^ int(CRCdividend[bit]))
        #remove zeros da esquerda
        removeZeros(byteFinal)
        #verifica se ainda restam bits para serem analisados no dividendo, se não houver finaliza a divisão
        if(len(CRCdividend) < len(CRCdivider)):
            stop = True
        else:
            #adiciona zeros restantes no byteFinal
            dif = len(CRCdividend) - len(CRCdivider)
            i = 0
            while (i < dif):
                byteFinal += '0'
                CRCdividend = CRCdividend[:-1] #remove os zeros da direita
    
    return hex(byteFinal).split('x')[-1]


def removeZeros(CRCdividend):
    for bit in CRCdividend:
        if (CRCdividend[bit] == '0'):
            CRCdividend[bit] = ''
    return CRCdividend