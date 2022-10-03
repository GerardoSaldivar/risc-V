function traducirTipoR(str){
    let p0 = str[0]
    let tipo = str[1]// instruccion
    let rd = str[2]// rd
    let rs1 = str[3]// rs1
    let rs2 = str[4]// rs2
    let traduccion = ''
    $.ajax({
        async: false,
        url: '/'+tipo+'',
        type: 'GET',
        data: {'rs2':rs2,'rs1':rs1,"rd":rd},
        success: function(data){
            
            let = func7 = data[''+tipo+'']['func7']
            let = rs2 = data[''+tipo+'']['rs2']
            let = rs1 = data[''+tipo+'']['rs1']
            let = func3 = data[''+tipo+'']['func3']
            let = rd = data[''+tipo+'']['rd']
            let = opcode = data[''+tipo+'']['opcode']
            
            traduccion = func7+rs2+rs1+func3+rd+opcode         
        },
        error: function(error){
            console.log('error: '+error)
        }
    })
    return traduccion
}
function traducirTipoRE(str){
    let p0 = str[0]
    let etiqueta = str[1]
    let tipo = str[2]// instruccion
    let rd = str[3]// rd
    let rs1 = str[4]// rs1
    let rs2 = str[5]// rs2
    let traduccion = ''
    $.ajax({
        async: false,
        url: '/'+tipo+'',
        type: 'GET',
        data: {'rs2':rs2,'rs1':rs1,"rd":rd},
        success: function(data){
            
            let = func7 = data[''+tipo+'']['func7']
            let = rs2 = data[''+tipo+'']['rs2']
            let = rs1 = data[''+tipo+'']['rs1']
            let = func3 = data[''+tipo+'']['func3']
            let = rd = data[''+tipo+'']['rd']
            let = opcode = data[''+tipo+'']['opcode']
            
            traduccion = func7+rs2+rs1+func3+rd+opcode         
        },
        error: function(error){
            console.log('error: '+error)
        }
    })
    return traduccion
}
function traducirTipoI(str){
    let p0 = str[0]
    let tipo = str[1]// instruccion
    let rd = str[2]// rd
    let rs1 = str[3]// rs1
    let inm = str[4]// inm
    let traduccion = ''
    $.ajax({
        async: false,
        url: '/'+tipo+'',
        type: 'GET',
        data:  {'inm':inm,'rs1':rs1,"rd":rd},
        success: function(data){
            
            let = inm = data[''+tipo+'']['inmediato']
            let = rs1 = data[''+tipo+'']['rs1']
            let = func3 = data[''+tipo+'']['func3']
            let = rd = data[''+tipo+'']['rd']
            let = opcode = data[''+tipo+'']['opcode']
            
            traduccion = inm+rs1+func3+rd+opcode          
        },
        error: function(error){
            console.log('error: '+error)
        }
    })
    return traduccion
}
function traducirTipoIE(str){
    let p0 = str[0]
    let etiqueta = str[1]
    let tipo = str[2]// instruccion
    let rd = str[3]// rd
    let rs1 = str[4]// rs1
    let inm = str[5]// inm
    let traduccion = ''
    $.ajax({
        async: false,
        url: '/'+tipo+'',
        type: 'GET',
        data:  {'inm':inm,'rs1':rs1,"rd":rd},
        success: function(data){
            
            let = inm = data[''+tipo+'']['inmediato']
            let = rs1 = data[''+tipo+'']['rs1']
            let = func3 = data[''+tipo+'']['func3']
            let = rd = data[''+tipo+'']['rd']
            let = opcode = data[''+tipo+'']['opcode']
            
            traduccion = inm+rs1+func3+rd+opcode          
        },
        error: function(error){
            console.log('error: '+error)
        }
    })
    return traduccion
}

function traducirTipoLoadI(str){
    let p0 = str[0]
    let tipo = str[1]// instruccion
    let rs1 = str[2]// rs1
    let inm = str[3]// inm
    let rd = str[4]// rd
    let traduccion = ''
    $.ajax({
        async: false,
        url: '/'+tipo+'',
        type: 'GET',
        data:  {'inm':inm,'rs1':rs1,"rd":rd},
        success: function(data){
            
            let = opcode = data[''+tipo+'']['opcode']
            let = rd = data[''+tipo+'']['rd']
            let = func3 = data[''+tipo+'']['func3']
            let = rs1 = data[''+tipo+'']['rs1']
            let = inm = data[''+tipo+'']['inmediato']
            
            traduccion = inm+rs1+func3+rd+opcode         
        },
        error: function(error){
            console.log('error: '+error)
        }
    })
    return traduccion
}
function traducirTipoLoadIE(str){
    let p0 = str[0]
    let etiqueta = str[1]
    let tipo = str[2]// instruccion
    let rs1 = str[3]// rs1
    let inm = str[4]// inm
    let rd = str[5]// rd
    let traduccion = ''
    $.ajax({
        async: false,
        url: '/'+tipo+'',
        type: 'GET',
        data:  {'inm':inm,'rs1':rs1,"rd":rd},
        success: function(data){
            
            let = opcode = data[''+tipo+'']['opcode']
            let = rd = data[''+tipo+'']['rd']
            let = func3 = data[''+tipo+'']['func3']
            let = rs1 = data[''+tipo+'']['rs1']
            let = inm = data[''+tipo+'']['inmediato']
            
            traduccion = inm+rs1+func3+rd+opcode         
        },
        error: function(error){
            console.log('error: '+error)
        }
    })
    return traduccion
}

function traducirTipoStoreS(str){
    let p0 = str[0]
    let tipo = str[1]// instruccion
    let rs2 = str[2]// rs2
    let inm = str[3]// inm
    let rs1 = str[4]// rs1
    let traduccion = ''
    $.ajax({
        async: false,
        url: '/'+tipo+'',
        type: 'GET',
        data:  {'inm':inm,'rs1':rs1,"rs2":rs2},
        success: function(data){
            
            let = opcode = data[''+tipo+'']['opcode']
            let = inm5 = data[''+tipo+'']['inmediato5']
            let = func3 = data[''+tipo+'']['func3']
            let = rs1 = data[''+tipo+'']['rs1']
            let = rs2 = data[''+tipo+'']['rs2']
            let = inm7 = data[''+tipo+'']['inmediato7']
            
            traduccion = inm7+rs2+rs1+func3+inm5+opcode         
        },
        error: function(error){
            console.log('error: '+error)
        }
    })
    return traduccion
}

function traducirTipoStoreSE(str){
    let p0 = str[0]
    let etiqueta = str[1]
    let tipo = str[2]// instruccion
    let rs2 = str[3]// rs2
    let inm = str[4]// inm
    let rs1 = str[5]// rs1
    let traduccion = ''
    $.ajax({
        async: false,
        url: '/'+tipo+'',
        type: 'GET',
        data:  {'inm':inm,'rs1':rs1,"rs2":rs2},
        success: function(data){

            let = opcode = data[''+tipo+'']['opcode']
            let = inm5 = data[''+tipo+'']['inmediato5']
            let = func3 = data[''+tipo+'']['func3']
            let = rs1 = data[''+tipo+'']['rs1']
            let = rs2 = data[''+tipo+'']['rs2']
            let = inm7 = data[''+tipo+'']['inmediato7']
            
            traduccion = inm7+rs2+rs1+func3+inm5+opcode         
        },
        error: function(error){
            console.log('error: '+error)
        }
    })
    return traduccion
}

function traducirTiposHexadecimales(str){
    let p0 = str[0]
    let tipo = str[1]// instruccion
    let numhexa = str[2]// hexa
    let traduccion = ''
    $.ajax({
        async: false,
        url: '/'+tipo+'',
        type: 'GET',
        data:  {'numhexa':numhexa},
        success: function(data){
            
            let = hexa = data[''+tipo+'']['hexa']
            let = ceros = data[''+tipo+'']['ceros']
            
            traduccion = ceros+hexa
        },
        error: function(error){
            console.log('error: '+error)
        }
    })
    return traduccion
}
function traducirTiposHexadecimalesE(str){
    let p0 = str[0]
    let etiqueta = str[1]
    let tipo = str[2]// instruccion
    let numhexa = str[3]// hexa
    let traduccion = ''
    $.ajax({
        async: false,
        url: '/'+tipo+'',
        type: 'GET',
        data:  {'numhexa':numhexa},
        success: function(data){
            
            let = hexa = data[''+tipo+'']['hexa']
            let = ceros = data[''+tipo+'']['ceros']
            
            traduccion = ceros+hexa
        },
        error: function(error){
            console.log('error: '+error)
        }
    })
    return traduccion
}

function traducirTipoPTO(str){
    let p0 = str[0]
    let tipo = str[1]// instruccion
    let rs1 = str[2]// sr1
    let numhexa = str[3]// hexa

    let traduccion = ''
    $.ajax({
        async: false,
        url: '/'+tipo+'',
        type: 'GET',
        data:  {'numhexa':numhexa, 'rs1':rs1},
        success: function(data){
            
            let = ceros11 = data[''+tipo+'']['ceros11']
            let = rs1 = data[''+tipo+'']['rs1']
            let = ceros10 = data[''+tipo+'']['ceros10']
            let = hexa = data[''+tipo+'']['hexa']
            
            traduccion = ceros11+rs1+ceros10+hexa
        },
        error: function(error){
            console.log('error: '+error)
        }
    })
    return traduccion
}

function traducirTipoPTOE(str){
    let p0 = str[0]
    let etiqueta = str[1]
    let tipo = str[2]// instruccion
    let rs1 = str[3]// sr1
    let numhexa = str[4]// hexa

    let traduccion = ''
    $.ajax({
        async: false,
        url: '/'+tipo+'',
        type: 'GET',
        data:  {'numhexa':numhexa, 'rs1':rs1},
        success: function(data){
            
            let = ceros11 = data[''+tipo+'']['ceros11']
            let = rs1 = data[''+tipo+'']['rs1']
            let = ceros10 = data[''+tipo+'']['ceros10']
            let = hexa = data[''+tipo+'']['hexa']
            
            traduccion = ceros11+rs1+ceros10+hexa
        },
        error: function(error){
            console.log('error: '+error)
        }
    })
    return traduccion
}

function traducirTipoB(str){
    let p0 = str[0]
    let tipo = str[1]// instruccion
    let rs1 = str[2]// sr1
    let rs2 = str[3]// sr2
    let inm = str[4]// etiqueta

    //if(etiquetas.has(inm)){}else{}

    let valorHexa = etiquetas.get(inm)
    let num1 = HexadecimalADecimal(valorHexa)
    let num2 = HexadecimalADecimal(p0)
    let distancia = ''

    distancia = num1 - num2

    let traduccion = ''
    $.ajax({
        async: false,
        url: '/'+tipo+'',
        type: 'GET',
        data:  {'inm':distancia, 'rs1':rs1, 'rs2':rs2},
        success: function(data){
            
            let = opcode = data[''+tipo+'']['opcode']
            let = inm5 = data[''+tipo+'']['inmediato5']
            let = func3 = data[''+tipo+'']['func3']
            let = rs1 = data[''+tipo+'']['rs1']
            let = rs2 = data[''+tipo+'']['rs2']
            let = inm7 = data[''+tipo+'']['inmediato7']
            
            traduccion = inm7+rs2+rs1+func3+inm5+opcode
        },
        error: function(error){
            console.log('error: '+error)
        }
    })
    return traduccion
}