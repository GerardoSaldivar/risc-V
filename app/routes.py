from flask import request, jsonify
from app import app
from .OperacionesBinarias import convertirBinarios, HexadecimalBinario, convertirPunteros

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
        "tipo anexadas":"pto, reti, shot"
    }}),200

@app.route('/add', methods = ['GET'])
def add():
    rs2 = request.args.get('rs2')
    rs1 = request.args.get('rs1')
    rd = request.args.get('rd')

    return jsonify({ "add":{
        "func7": "0000000",
        "func3": "000",
        "opcode": "0110011",
        "rs2": "-----" if rs2 == None else convertirPunteros(rs2),
        "rs1": "-----" if rs1 == None else convertirPunteros(rs1),
        "rd": "-----" if rd == None else convertirPunteros(rd)
    }}),200,200

@app.route('/sub', methods = ['GET'])
def sub():
    rs2 = request.args.get('rs2')
    rs1 = request.args.get('rs1')
    rd = request.args.get('rd')
    
    return jsonify({ "sub":{
        "func7": "0100000",
        "func3": "000",
        "opcode": "0110011",
        "rs2": "-----" if rs2 == None else convertirPunteros(rs2),
        "rs1": "-----" if rs1 == None else convertirPunteros(rs1),
        "rd": "-----" if rd == None else convertirPunteros(rd)
    }}),200

@app.route('/sll', methods = ['GET'])
def sll():
    rs2 = request.args.get('rs2')
    rs1 = request.args.get('rs1')
    rd = request.args.get('rd')

    return jsonify({ "sll":{
        "func7": "0000000",
        "func3": "001",
        "opcode": "0110011",
        "rs2": "-----" if rs2 == None else convertirPunteros(rs2),
        "rs1": "-----" if rs1 == None else convertirPunteros(rs1),
        "rd": "-----" if rd == None else convertirPunteros(rd)
    }}),200

@app.route('/slt', methods = ['GET'])
def slt():
    rs2 = request.args.get('rs2')
    rs1 = request.args.get('rs1')
    rd = request.args.get('rd')

    return jsonify({ "slt":{
        "func7": "0000000",
        "func3": "010",
        "opcode": "0110011",
        "rs2": "-----" if rs2 == None else convertirPunteros(rs2),
        "rs1": "-----" if rs1 == None else convertirPunteros(rs1),
        "rd": "-----" if rd == None else convertirPunteros(rd)
    }}),200

@app.route('/sltu', methods = ['GET'])
def sltu():
    rs2 = request.args.get('rs2')
    rs1 = request.args.get('rs1')
    rd = request.args.get('rd')

    return jsonify({ "sltu":{
        "func7": "0000000",
        "func3": "011",
        "opcode": "0110011",    
        "rs2": "-----" if rs2 == None else convertirPunteros(rs2),
        "rs1": "-----" if rs1 == None else convertirPunteros(rs1),
        "rd": "-----" if rd == None else convertirPunteros(rd)
    }}),200

@app.route('/xor', methods = ['GET'])
def xor():
    rs2 = request.args.get('rs2')
    rs1 = request.args.get('rs1')
    rd = request.args.get('rd')

    return jsonify({ "xor":{
        "func7": "0000000",
        "func3": "100",
        "opcode": "0110011",    
        "rs2": "-----" if rs2 == None else convertirPunteros(rs2),
        "rs1": "-----" if rs1 == None else convertirPunteros(rs1),
        "rd": "-----" if rd == None else convertirPunteros(rd)
    }}),200

@app.route('/srl', methods = ['GET'])
def srl():
    rs2 = request.args.get('rs2')
    rs1 = request.args.get('rs1')
    rd = request.args.get('rd')

    return jsonify({ "srl":{
        "func7": "0000000",
        "func3": "101",
        "opcode": "0110011",    
        "rs2": "-----" if rs2 == None else convertirPunteros(rs2),
        "rs1": "-----" if rs1 == None else convertirPunteros(rs1),
        "rd": "-----" if rd == None else convertirPunteros(rd)
    }}),200

@app.route('/sra', methods = ['GET'])
def sra():
    rs2 = request.args.get('rs2')
    rs1 = request.args.get('rs1')
    rd = request.args.get('rd')

    return jsonify({ "sra":{
        "func7": "0100000",
        "func3": "101",
        "opcode": "0110011",    
        "rs2": "-----" if rs2 == None else convertirPunteros(rs2),
        "rs1": "-----" if rs1 == None else convertirPunteros(rs1),
        "rd": "-----" if rd == None else convertirPunteros(rd)
    }}),200

@app.route('/or', methods = ['GET'])
def orr():
    rs2 = request.args.get('rs2')
    rs1 = request.args.get('rs1')
    rd = request.args.get('rd')

    return jsonify({ "or":{
        "func7": "0000000",
        "func3": "110",
        "opcode": "0110011",    
        "rs2": "-----" if rs2 == None else convertirPunteros(rs2),
        "rs1": "-----" if rs1 == None else convertirPunteros(rs1),
        "rd": "-----" if rd == None else convertirPunteros(rd)
    }}),200,200

@app.route('/and', methods = ['GET'])
def andd():
    rs2 = request.args.get('rs2')
    rs1 = request.args.get('rs1')
    rd = request.args.get('rd')

    return jsonify({ "and":{
        "func7": "0000000",
        "func3": "111",
        "opcode": "0110011",    
        "rs2": "-----" if rs2 == None else convertirPunteros(rs2),
        "rs1": "-----" if rs1 == None else convertirPunteros(rs1),
        "rd": "-----" if rd == None else convertirPunteros(rd)
    }}),200,200

@app.route('/addi', methods = ['GET'])
def addi():
    rs1 = request.args.get('rs1')
    rd = request.args.get('rd')
    inm = request.args.get('inm')

    return jsonify({ "addi":{
        "inmediato": "-----" if inm == None else convertirBinarios(inm),
        "func3": "000",
        "opcode": "0010011",
        "rs1": "-----" if rs1 == None else convertirPunteros(rs1),
        "rd": "-----" if rd == None else convertirPunteros(rd)
    }}),200

@app.route('/andi', methods = ['GET'])
def andi():
    rs1 = request.args.get('rs1')
    rd = request.args.get('rd')
    inm = request.args.get('inm')

    return jsonify({ "andi":{
        "inmediato": "-----" if inm == None else convertirBinarios(inm),
        "func3": "111",
        "opcode": "0010011",
        "rs1": "-----" if rs1 == None else convertirPunteros(rs1),
        "rd": "-----" if rd == None else convertirPunteros(rd)
    }}),200,200

@app.route('/ori', methods = ['GET'])
def ori():
    rs1 = request.args.get('rs1')
    rd = request.args.get('rd')
    inm = request.args.get('inm')

    return jsonify({ "ori":{
        "inmediato": "-----" if inm == None else convertirBinarios(inm),
        "func3": "110",
        "opcode": "0010011",
        "rs1": "-----" if rs1 == None else convertirPunteros(rs1),
        "rd": "-----" if rd == None else convertirPunteros(rd)
    }}),200

@app.route('/xori', methods = ['GET'])
def xori():
    rs1 = request.args.get('rs1')
    rd = request.args.get('rd')
    inm = request.args.get('inm')

    return jsonify({ "xori":{
        "inmediato": "-----" if inm == None else convertirBinarios(inm),
        "func3": "100",
        "opcode": "0010011",
        "rs1": "-----" if rs1 == None else convertirPunteros(rs1),
        "rd": "-----" if rd == None else convertirPunteros(rd)
    }}),200

@app.route('/slti', methods = ['GET'])
def slti():
    rs1 = request.args.get('rs1')
    rd = request.args.get('rd')
    inm = request.args.get('inm')

    return jsonify({ "slti":{
        "inmediato": "-----" if inm == None else convertirBinarios(inm),
        "func3": "010",
        "opcode": "0010011",
        "rs1": "-----" if rs1 == None else convertirPunteros(rs1),
        "rd": "-----" if rd == None else convertirPunteros(rd)
    }}),200

@app.route('/sltiu', methods = ['GET'])
def sltui():
    rs1 = request.args.get('rs1')
    rd = request.args.get('rd')
    inm = request.args.get('inm')

    return jsonify({ "sltiu":{
        "inmediato": "-----" if inm == None else convertirBinarios(inm),
        "func3": "011",
        "opcode": "0010011",
        "rs1": "-----" if rs1 == None else convertirPunteros(rs1),
        "rd": "-----" if rd == None else convertirPunteros(rd)
    }}),200

@app.route('/slli', methods = ['GET'])
def slli():
    rs1 = request.args.get('rs1')
    rd = request.args.get('rd')
    inm = request.args.get('inm')

    return jsonify({ "slli":{
        "inmediato": "-----" if inm == None else convertirBinarios(inm),
        "func3": "001",
        "opcode": "0010011",
        "rs1": "-----" if rs1 == None else convertirPunteros(rs1),
        "rd": "-----" if rd == None else convertirPunteros(rd)
    }}),200

@app.route('/srli', methods = ['GET'])
def srli():
    rs1 = request.args.get('rs1')
    rd = request.args.get('rd')
    inm = request.args.get('inm')

    return jsonify({ "srli":{
        "inmediato": "-----" if inm == None else convertirBinarios(inm),
        "func3": "101",
        "opcode": "0010011",
        "rs1": "-----" if rs1 == None else convertirPunteros(rs1),
        "rd": "-----" if rd == None else convertirPunteros(rd)
    }}),200

@app.route('/srai', methods = ['GET'])
def srai():
    rs1 = request.args.get('rs1')
    rd = request.args.get('rd')
    inm = request.args.get('inm')

    return jsonify({ "srai":{
        "inmediato": "-----" if inm == None else convertirBinarios(inm),
        "func3": "100",
        "opcode": "0010011",
        "rs1": "-----" if rs1 == None else convertirPunteros(rs1),
        "rd": "-----" if rd == None else convertirPunteros(rd)
    }}),200

@app.route('/lb', methods = ['GET'])
def lb():
    rs1 = request.args.get('rs1')
    rd = request.args.get('rd')

    numero = request.args.get('inm')
    numconv = convertirBinarios(numero)
    return jsonify({ "lb":{
        "inmediato": numconv,
        "func3": "000",
        "opcode": "0000011",
        "rs1": "-----" if rs1 == None else convertirPunteros(rs1),
        "rd": "-----" if rd == None else convertirPunteros(rd)
    }}),200

@app.route('/lh', methods = ['GET'])
def lh():
    rs1 = request.args.get('rs1')
    rd = request.args.get('rd')

    numero = request.args.get('inm')
    numconv = convertirBinarios(numero)
    return jsonify({ "lh":{
        "inmediato": numconv,
        "func3": "001",
        "opcode": "0000011",
        "rs1": "-----" if rs1 == None else convertirPunteros(rs1),
        "rd": "-----" if rd == None else convertirPunteros(rd)
    }}),200

@app.route('/lw', methods = ['GET'])
def lw():
    rs1 = request.args.get('rs1')
    rd = request.args.get('rd')

    numero = request.args.get('inm')
    numconv = convertirBinarios(numero)
    return jsonify({ "lw":{
        "inmediato": numconv,
        "func3": "010",
        "opcode": "0000011",
        "rs1": "-----" if rs1 == None else convertirPunteros(rs1),
        "rd": "-----" if rd == None else convertirPunteros(rd)
    }}),200

@app.route('/lbu', methods = ['GET'])
def lbu():
    rs1 = request.args.get('rs1')
    rd = request.args.get('rd')

    numero = request.args.get('inm')
    numconv = convertirBinarios(numero)
    return jsonify({ "lbu":{
        "inmediato": numconv,
        "func3": "100",
        "opcode": "0000011",
        "rs1": "-----" if rs1 == None else convertirPunteros(rs1),
        "rd": "-----" if rd == None else convertirPunteros(rd)
    }}),200

@app.route('/lhu', methods = ['GET'])
def lhu():
    rs1 = request.args.get('rs1')
    rd = request.args.get('rd')

    numero = request.args.get('inm')
    numconv = convertirBinarios(numero)
    return jsonify({ "lhu":{
        "inmediato": numconv,
        "func3": "101",
        "opcode": "0000011",
        "rs1": "-----" if rs1 == None else convertirPunteros(rs1),
        "rd": "-----" if rd == None else convertirPunteros(rd)
    }}),200

@app.route('/sb', methods = ['GET'])
def sb():
    rs1 = request.args.get('rs1')
    rd = request.args.get('rd')
    numero = request.args.get('inm')
    numconv = convertirBinarios(numero)
    num5 = numconv[7:12]
    num7 = numconv[0:7]
    return jsonify({ "sb":{
        "inmediato5": num5,
        "inmediato7": num7,
        "func3": "000",
        "opcode": "0100011",
        "rs1": "-----" if rs1 == None else convertirPunteros(rs1),
        "rd": "-----" if rd == None else convertirPunteros(rd)
    }}),200

@app.route('/sh', methods = ['GET'])
def sh():
    rs1 = request.args.get('rs1')
    rd = request.args.get('rd')
    numero = request.args.get('inm')
    numconv = convertirBinarios(numero)
    num5 = numconv[7:12]
    num7 = numconv[0:7]
    return jsonify({ "sh":{
        "inmediato5": num5,
        "inmediato7": num7,
        "func3": "001",
        "opcode": "0100011",
        "rs1": "-----" if rs1 == None else convertirPunteros(rs1),
        "rd": "-----" if rd == None else convertirPunteros(rd),
    }}),200

@app.route('/sw', methods = ['GET'])
def sw():
    rs1 = request.args.get('rs1')
    rd = request.args.get('rd')
    numero = request.args.get('inm')
    numconv = convertirBinarios(numero)
    num5 = numconv[7:12]
    num7 = numconv[0:7]
    return jsonify({ "sw":{
        "inmediato5": num5,
        "inmediato7": num7,
        "func3": "010",
        "opcode": "0100011",
        "rs1": "-----" if rs1 == None else convertirPunteros(rs1),
        "rd": "-----" if rd == None else convertirPunteros(rd)
    }}),200

@app.route('/reti', methods = ['GET'])
def reti():
    num = request.args.get('numhexa')
    numConv = HexadecimalBinario(num)
    return jsonify({ "reti":{
        "ceros": "00000000000000000000000000",#26
        "hexa": numConv
    }}),200

@app.route('/shot', methods = ['GET'])
def shot():
    num = request.args.get('numhexa')
    numConv = HexadecimalBinario(num)
    return jsonify({ "shot":{
        "ceros": "00000000000000000000000000",#26
        "hexa": numConv
    }}),200

@app.route('/pto', methods = ['GET'])
def pto():
    rs1 = request.args.get('rs1')
    num = request.args.get('numhexa')
    numConv = HexadecimalBinario(num)
    return jsonify({ "pto":{
        "ceros11": "00000000000",
        "rs1": convertirPunteros(rs1),
        "ceros10": "0000000000",
        "hexa": numConv
    }}),200

@app.route('/beq', methods = ['GET'])
def beq():
    rs1 = request.args.get('rs1')
    rd = request.args.get('rd')
    numero = request.args.get('inm')
    if numero == None:
        num4, num6, num11, num12 = "-----","-----","-----","-----"
    else:
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
        "rs1": "-----" if rs1 == None else convertirPunteros(rs1),
        "rd": "-----" if rd == None else convertirPunteros(rd),
    }}),200

@app.route('/bne', methods = ['GET'])
def bne():
    rs1 = request.args.get('rs1')
    rd = request.args.get('rd')
    numero = request.args.get('inm')
    if numero == None:
        num4, num6, num11, num12 = "-----","-----","-----","-----"
    else:
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
        "rs1": "-----" if rs1 == None else convertirPunteros(rs1),
        "rd": "-----" if rd == None else convertirPunteros(rd),
    }}),200

@app.route('/blt', methods = ['GET'])
def blt():
    rs1 = request.args.get('rs1')
    rd = request.args.get('rd')
    numero = request.args.get('inm')
    if numero == None:
        num4, num6, num11, num12 = "-----","-----","-----","-----"
    else:
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
        "rs1": "-----" if rs1 == None else convertirPunteros(rs1),
        "rd": "-----" if rd == None else convertirPunteros(rd),
    }}),200

@app.route('/bge', methods = ['GET'])
def bge():
    rs1 = request.args.get('rs1')
    rd = request.args.get('rd')
    numero = request.args.get('inm')
    if numero == None:
        num4, num6, num11, num12 = "-----","-----","-----","-----"
    else:
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
        "rs1": "-----" if rs1 == None else convertirPunteros(rs1),
        "rd": "-----" if rd == None else convertirPunteros(rd),
    }}),200

@app.route('/bltu', methods = ['GET'])
def bltu():
    rs1 = request.args.get('rs1')
    rd = request.args.get('rd')
    numero = request.args.get('inm')
    if numero == None:
        num4, num6, num11, num12 = "-----","-----","-----","-----"
    else:
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
        "rs1": "-----" if rs1 == None else convertirPunteros(rs1),
        "rd": "-----" if rd == None else convertirPunteros(rd),
    }}),200

@app.route('/bgeu', methods = ['GET'])
def bgeu():
    rs1 = request.args.get('rs1')
    rd = request.args.get('rd')
    numero = request.args.get('inm')
    if numero == None:
        num4, num6, num11, num12 = "-----","-----","-----","-----"
    else:
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
        "rs1": "-----" if rs1 == None else convertirPunteros(rs1),
        "rd": "-----" if rd == None else convertirPunteros(rd),
    }}),200