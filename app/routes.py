from flask import render_template, request, jsonify
from app import app
from .OperacionesBinarias import punteros, convertirBinarios, HexadecimalBinario

@app.route('/', methods = ['GET'])
def inicio():
    return jsonify({ "inicio":{
        "app": "API",
        "procesador": "Risc - V",
        "tipo R": "add, sub, sll, slt, sltu, xor, srl, sra, or, and",
        "tipo I": "addi, andi, ori, xori, slti, sltiu, slli, srli, srai",
        "tipo load (i)": "lb, lh, lw, lbu, lhu",
        "tipo store (s)": "sb, sh, sw",
        "tipo B": "beq, bne, blt, bge, bltu, bgeu",
        "anexadas":"pto, reti, shot"
    }})

@app.route('/add', methods = ['GET'])
def add():
    return jsonify({ "add":{
        "func7": "0000000",
        "func3": "000",
        "opcode": "0110011",
        "rs2": punteros[request.args.get('rs2')],
        "rs1": punteros[request.args.get('rs1')],
        "rd": punteros[request.args.get('rd')]
    }})

@app.route('/sub', methods = ['GET'])
def sub():
    return jsonify({ "sub":{
        "func7": "0100000",
        "func3": "000",
        "opcode": "0110011",
        "rs2": punteros[request.args.get('rs2')],
        "rs1": punteros[request.args.get('rs1')],
        "rd": punteros[request.args.get('rd')]
    }})

@app.route('/sll', methods = ['GET'])
def sll():
    return jsonify({ "sll":{
        "func7": "0000000",
        "func3": "001",
        "opcode": "0110011",
        "rs2": punteros[request.args.get('rs2')],
        "rs1": punteros[request.args.get('rs1')],
        "rd": punteros[request.args.get('rd')]
    }})

@app.route('/slt', methods = ['GET'])
def slt():
    return jsonify({ "slt":{
        "func7": "0000000",
        "func3": "010",
        "opcode": "0110011",
        "rs2": punteros[request.args.get('rs2')],
        "rs1": punteros[request.args.get('rs1')],
        "rd": punteros[request.args.get('rd')]
    }})

@app.route('/sltu', methods = ['GET'])
def sltu():
    return jsonify({ "sltu":{
        "func7": "0000000",
        "func3": "011",
        "opcode": "0110011",    
        "rs2": punteros[request.args.get('rs2')],
        "rs1": punteros[request.args.get('rs1')],
        "rd": punteros[request.args.get('rd')]
    }})

@app.route('/xor', methods = ['GET'])
def xor():
    return jsonify({ "xor":{
        "func7": "0000000",
        "func3": "100",
        "opcode": "0110011",    
        "rs2": punteros[request.args.get('rs2')],
        "rs1": punteros[request.args.get('rs1')],
        "rd": punteros[request.args.get('rd')]
    }})

@app.route('/srl', methods = ['GET'])
def srl():
    return jsonify({ "srl":{
        "func7": "0000000",
        "func3": "101",
        "opcode": "0110011",    
        "rs2": punteros[request.args.get('rs2')],
        "rs1": punteros[request.args.get('rs1')],
        "rd": punteros[request.args.get('rd')]
    }})

@app.route('/sra', methods = ['GET'])
def sra():
    return jsonify({ "sra":{
        "func7": "0100000",
        "func3": "101",
        "opcode": "0110011",    
        "rs2": punteros[request.args.get('rs2')],
        "rs1": punteros[request.args.get('rs1')],
        "rd": punteros[request.args.get('rd')]
    }})

@app.route('/or', methods = ['GET'])
def orr():
    return jsonify({ "or":{
        "func7": "0000000",
        "func3": "110",
        "opcode": "0110011",    
        "rs2": punteros[request.args.get('rs2')],
        "rs1": punteros[request.args.get('rs1')],
        "rd": punteros[request.args.get('rd')]
    }})

@app.route('/and', methods = ['GET'])
def andd():
    return jsonify({ "and":{
        "func7": "0000000",
        "func3": "111",
        "opcode": "0110011",    
        "rs2": punteros[request.args.get('rs2')],
        "rs1": punteros[request.args.get('rs1')],
        "rd": punteros[request.args.get('rd')]
    }})

@app.route('/addi', methods = ['GET'])
def addi():
    return jsonify({ "addi":{
        "inmediato": convertirBinarios(request.args.get('inm')),
        "func3": "000",
        "opcode": "0010011",
        "rs1": punteros[request.args.get('rs1')],
        "rd": punteros[request.args.get('rd')]
    }})

@app.route('/andi', methods = ['GET'])
def andi():
    return jsonify({ "andi":{
        "inmediato": convertirBinarios(request.args.get('inm')),
        "func3": "111",
        "opcode": "0010011",
        "rs1": punteros[request.args.get('rs1')],
        "rd": punteros[request.args.get('rd')]
    }})

@app.route('/ori', methods = ['GET'])
def ori():
    return jsonify({ "ori":{
        "inmediato": convertirBinarios(request.args.get('inm')),
        "func3": "110",
        "opcode": "0010011",
        "rs1": punteros[request.args.get('rs1')],
        "rd": punteros[request.args.get('rd')]
    }})

@app.route('/xori', methods = ['GET'])
def xori():
    return jsonify({ "xori":{
        "inmediato": convertirBinarios(request.args.get('inm')),
        "func3": "100",
        "opcode": "0010011",
        "rs1": punteros[request.args.get('rs1')],
        "rd": punteros[request.args.get('rd')]
    }})

@app.route('/slti', methods = ['GET'])
def slti():
    return jsonify({ "slti":{
        "inmediato": convertirBinarios(request.args.get('inm')),
        "func3": "010",
        "opcode": "0010011",
        "rs1": punteros[request.args.get('rs1')],
        "rd": punteros[request.args.get('rd')]
    }})

@app.route('/sltiu', methods = ['GET'])
def sltui():
    return jsonify({ "sltiu":{
        "inmediato": convertirBinarios(request.args.get('inm')),
        "func3": "011",
        "opcode": "0010011",
        "rs1": punteros[request.args.get('rs1')],
        "rd": punteros[request.args.get('rd')]
    }})

@app.route('/slli', methods = ['GET'])
def slli():
    return jsonify({ "slli":{
        "inmediato": convertirBinarios(request.args.get('inm')),
        "func3": "001",
        "opcode": "0010011",
        "rs1": punteros[request.args.get('rs1')],
        "rd": punteros[request.args.get('rd')]
    }})

@app.route('/srli', methods = ['GET'])
def srli():
    return jsonify({ "srli":{
        "inmediato": convertirBinarios(request.args.get('inm')),
        "func3": "101",
        "opcode": "0010011",
        "rs1": punteros[request.args.get('rs1')],
        "rd": punteros[request.args.get('rd')]
    }})

@app.route('/srai', methods = ['GET'])
def srai():
    return jsonify({ "srai":{
        "inmediato": convertirBinarios(request.args.get('inm')),
        "func3": "100",
        "opcode": "0010011",
        "rs1": punteros[request.args.get('rs1')],
        "rd": punteros[request.args.get('rd')]
    }})

@app.route('/lb', methods = ['GET'])
def lb():
    numero = request.args.get('inm')
    numconv = convertirBinarios(numero)
    return jsonify({ "lb":{
        "inmediato": numconv,
        "func3": "000",
        "opcode": "0000011",
        "rs1": punteros[request.args.get('rs1')],
        "rd": punteros[request.args.get('rd')]
    }})

@app.route('/lh', methods = ['GET'])
def lh():
    numero = request.args.get('inm')
    numconv = convertirBinarios(numero)
    return jsonify({ "lh":{
        "inmediato": numconv,
        "func3": "001",
        "opcode": "0000011",
        "rs1": punteros[request.args.get('rs1')],
        "rd": punteros[request.args.get('rd')]
    }})

@app.route('/lw', methods = ['GET'])
def lw():
    numero = request.args.get('inm')
    numconv = convertirBinarios(numero)
    return jsonify({ "lw":{
        "inmediato": numconv,
        "func3": "010",
        "opcode": "0000011",
        "rs1": punteros[request.args.get('rs1')],
        "rd": punteros[request.args.get('rd')]
    }})

@app.route('/lbu', methods = ['GET'])
def lbu():
    numero = request.args.get('inm')
    numconv = convertirBinarios(numero)
    return jsonify({ "lbu":{
        "inmediato": numconv,
        "func3": "100",
        "opcode": "0000011",
        "rs1": punteros[request.args.get('rs1')],
        "rd": punteros[request.args.get('rd')]
    }})

@app.route('/lhu', methods = ['GET'])
def lhu():
    numero = request.args.get('inm')
    numconv = convertirBinarios(numero)
    return jsonify({ "lhu":{
        "inmediato": numconv,
        "func3": "101",
        "opcode": "0000011",
        "rs1": punteros[request.args.get('rs1')],
        "rd": punteros[request.args.get('rd')]
    }})

@app.route('/sb', methods = ['GET'])
def sb():
    numero = request.args.get('inm')
    numconv = convertirBinarios(numero)
    num5 = numconv[7:12]
    num7 = numconv[0:7]
    return jsonify({ "sb":{
        "inmediato5": num5,
        "inmediato7": num7,
        "func3": "000",
        "opcode": "0100011",
        "rs1": punteros[request.args.get('rs1')],
        "rs2": punteros[request.args.get('rs2')]
    }})

@app.route('/sh', methods = ['GET'])
def sh():
    numero = request.args.get('inm')
    numconv = convertirBinarios(numero)
    num5 = numconv[7:12]
    num7 = numconv[0:7]
    return jsonify({ "sh":{
        "inmediato5": num5,
        "inmediato7": num7,
        "func3": "001",
        "opcode": "0100011",
        "rs1": punteros[request.args.get('rs1')],
        "rs2": punteros[request.args.get('rs2')],
    }})

@app.route('/sw', methods = ['GET'])
def sw():
    numero = request.args.get('inm')
    numconv = convertirBinarios(numero)
    num5 = numconv[7:12]
    num7 = numconv[0:7]
    return jsonify({ "sw":{
        "inmediato5": num5,
        "inmediato7": num7,
        "func3": "010",
        "opcode": "0100011",
        "rs1": punteros[request.args.get('rs1')],
        "rs2": punteros[request.args.get('rs2')]
    }})

@app.route('/reti', methods = ['GET'])
def reti():
    num = request.args.get('numhexa')
    numConv = HexadecimalBinario(num)
    return jsonify({ "reti":{
        "ceros": "00000000000000000000000000",#26
        "hexa": numConv
    }})

@app.route('/shot', methods = ['GET'])
def shot():
    num = request.args.get('numhexa')
    numConv = HexadecimalBinario(num)
    return jsonify({ "shot":{
        "ceros": "00000000000000000000000000",#26
        "hexa": numConv
    }})

@app.route('/pto', methods = ['GET'])
def pto():
    num = request.args.get('numhexa')
    numConv = HexadecimalBinario(num)
    return jsonify({ "pto":{
        "ceros11": "00000000000",
        "rs1": punteros[request.args.get('rs1')],
        "ceros10": "0000000000",
        "hexa": numConv
    }})

@app.route('/beq', methods = ['GET'])
def beq():
    numero = request.args.get('inm')
    numconv = convertirBinarios(numero)
    num4 = numconv[8:12]
    num6 = numconv[2:8]
    num11 = numconv[1]
    num12 = numconv[0]
    return jsonify({ "beq":{
        "opcode": "1100011",
        "func3": "000",
        "inmediato5": num4+num11,
        "inmediato7": num12+num6,
        "rs1": punteros[request.args.get('rs1')],
        "rs2": punteros[request.args.get('rs2')],
    }})

@app.route('/bne', methods = ['GET'])
def bne():
    numero = request.args.get('inm')
    numconv = convertirBinarios(numero)
    num4 = numconv[8:12]
    num6 = numconv[2:8]
    num11 = numconv[1]
    num12 = numconv[0]
    return jsonify({ "bne":{
        "opcode": "1100011",
        "func3": "001",
        "inmediato5": num4+num11,
        "inmediato7": num12+num6,
        "rs1": punteros[request.args.get('rs1')],
        "rs2": punteros[request.args.get('rs2')],
    }})

@app.route('/blt', methods = ['GET'])
def blt():
    numero = request.args.get('inm')
    numconv = convertirBinarios(numero)
    num4 = numconv[8:12]
    num6 = numconv[2:8]
    num11 = numconv[1]
    num12 = numconv[0]
    return jsonify({ "blt":{
        "opcode": "1100011",
        "func3": "100",
        "inmediato5": num4+num11,
        "inmediato7": num12+num6,
        "rs1": punteros[request.args.get('rs1')],
        "rs2": punteros[request.args.get('rs2')],
    }})

@app.route('/bge', methods = ['GET'])
def bge():
    numero = request.args.get('inm')
    numconv = convertirBinarios(numero)
    num4 = numconv[8:12]
    num6 = numconv[2:8]
    num11 = numconv[1]
    num12 = numconv[0]
    return jsonify({ "bge":{
        "opcode": "1100011",
        "func3": "101",
        "inmediato5": num4+num11,
        "inmediato7": num12+num6,
        "rs1": punteros[request.args.get('rs1')],
        "rs2": punteros[request.args.get('rs2')],
    }})

@app.route('/bltu', methods = ['GET'])
def bltu():
    numero = request.args.get('inm')
    numconv = convertirBinarios(numero)
    num4 = numconv[8:12]
    num6 = numconv[2:8]
    num11 = numconv[1]
    num12 = numconv[0]
    return jsonify({ "bltu":{
        "opcode": "1100011",
        "func3": "110",
        "inmediato5": num4+num11,
        "inmediato7": num12+num6,
        "rs1": punteros[request.args.get('rs1')],
        "rs2": punteros[request.args.get('rs2')],
    }})

@app.route('/bgeu', methods = ['GET'])
def bgeu():
    numero = request.args.get('inm')
    numconv = convertirBinarios(numero)
    num4 = numconv[8:12]
    num6 = numconv[2:8]
    num11 = numconv[1]
    num12 = numconv[0]
    return jsonify({ "bgeu":{
        "opcode": "1100011",
        "func3": "111",
        "inmediato5": num4+num11,
        "inmediato7": num12+num6,
        "rs1": punteros[request.args.get('rs1')],
        "rs2": punteros[request.args.get('rs2')],
    }})