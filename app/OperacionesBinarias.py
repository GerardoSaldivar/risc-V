punteros = {
    'x0':'00000','X0':'00000',
    'x1':'00001','X1':'00001',
    'x2':'00010','X2':'00010',
    'x3':'00011','X3':'00011',
    'x4':'00100','X4':'00100',
    'x5':'00101','X5':'00101',
    'x6':'00110','X6':'00110',
    'x7':'00111','X7':'00111',
    'x8':'01000','X8':'01000',
    'x9':'01001','X9':'01001',
    'x10' : '01010','X10' : '01010',
    'x11' : '01011','X11' : '01011',
    'x12' : '01100','X12' : '01100',
    'x13' : '01101','X13' : '01101',
    'x14' : '01110','X14' : '01110',
    'x15' : '01111','X15' : '01111',
    'x16' : '10000','X16' : '10000',
    'x17' : '10001','X17' : '10001',
    'x18' : '10010','X18' : '10010',
    'x19' : '10011','X19' : '10011',
    'x20' : '10100','X20' : '10100',
    'x21' : '10101','X21' : '10101',
    'x22' : '10110','X22' : '10110',
    'x23' : '10111','X23' : '10111',
    'x24' : '11000','X24' : '11000',
    'x25' : '11001','X25' : '11001',
    'x26' : '11010','X26' : '11010',
    'x27' : '11011','X27' : '11011',
    'x28' : '11100','X28' : '11100',
    'x29' : '11101','X29' : '11101',
    'x30' : '11110','X30' : '11110',
    'x31' : '11111','X31' : '11111'
}

def convertirBinarios(num2):
    num, salida = "",""

    try:
        num = int(num2)
    except:
        salida = "------------"

    if (isinstance(num, int)):
        num = int(num2)
        if(num >= 0 and num <= 2047):
            temp = format(num, "b")
            salida = formato12(temp)
        if(num >= -2048 and num <= -1):
            temp = num * -1
            temp2 = format(temp, "b")
            formato = formato12(temp2)
            temp3 = formato.replace('1','2')
            temp4 = temp3.replace('0','1')
            temp5 = temp4.replace('2','0')
            temp6 = int(temp5,2)
            temp7 = temp6 + 1
            salida = format(temp7, 'b')
        if(num <= -2049 or num >= 2048 ):
            salida = "------------"
    else:
        salida = "------------"
    return str(salida)

def formato12(num):
    num1 = str(num)
    while len(num1) < 12:
        num1 = '0'+num1
    return num1

def HexadecimalBinario(numHex):
    numDec = int(numHex,16)
    numBin = format(numDec, "b")
    numBinStr = str(numBin)
    while len(numBinStr) < 5:
        numBinStr = '0'+numBinStr
    return numBinStr

#def imprimirBinarios():
#    num = -2048
#    while ( num <= 2047 ):
#        numbinario = convertirBinarios(num)
#        print(num,numbinario)
#        num = num + 1