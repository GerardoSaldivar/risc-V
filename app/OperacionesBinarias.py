import re

def convertirPunteros(p):
    salida = ""
    numbers = re.findall('\d', p)

    try:
        t = int(p)
        salida = ""
    except:
        if len(numbers) == 1:
            i = int(numbers[0])
            b = format(i, "b")
            num = int(b)
            f = formato5(num)
            salida = f
        if len(numbers) > 1:
            j = ",".join(numbers)
            r = j.replace(",","")
            i = int(r)
            b = format(i, "b")
            salida = "-----" if i > 31 else formato5(b)

    return "-----" if len(salida) == 0 else salida


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

def formato5(num):
    num1 = str(num)
    while len(num1) < 5:
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