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

punteros = {
    'x0':'00000','zero':'00000',
    'x1':'00001','ra':'00001',
    'x2':'00010','sp':'00010',
    'x3':'00011','gp':'00011',
    'x4':'00100','tp':'00100',
    'x5':'00101','t0':'00101',
    'x6':'00110','t1':'00110',
    'x7':'00111','t2':'00111',
    'x8':'01000','s0':'01000','fp':'01000',
    'x9':'01001','s1':'01001',
    'x10' : '01010','a0' : '01010',
    'x11' : '01011','a1' : '01011',
    'x12' : '01100','a2' : '01100',
    'x13' : '01101','a3' : '01101',
    'x14' : '01110','a4' : '01110',
    'x15' : '01111','a5' : '01111',
    'x16' : '10000','a6' : '10000',
    'x17' : '10001','a7' : '10001',
    'x18' : '10010','s2' : '10010',
    'x19' : '10011','s3' : '10011',
    'x20' : '10100','s4' : '10100',
    'x21' : '10101','s5' : '10101',
    'x22' : '10110','s6' : '10110',
    'x23' : '10111','s7' : '10111',
    'x24' : '11000','s8' : '11000',
    'x25' : '11001','s9' : '11001',
    'x26' : '11010','s10' : '11010',
    'x27' : '11011','s11' : '11011',
    'x28' : '11100','t3' : '11100',
    'x29' : '11101','t4' : '11101',
    'x30' : '11110','t5' : '11110',
    'x31' : '11111','t6' : '11111'
}

def convertirRegistro(r):
    salida = ''
    try:
        m = r.lower()
        salida = punteros[m]
    except:
        salida = '-----'
    return salida