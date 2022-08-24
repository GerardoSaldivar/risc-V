let num = 0;
$(document).ready(function(){
    let str = document.getElementById("textIn").value.trim()
    if(str === ""){
        $("#textIn").val('0000')
    }else{
        console.log("no vacio")
    }

    $('a[data-toggle="tab"]').on('show.bs.tab', function(e) {
		localStorage.setItem('activeTab', $(e.target).attr('href'));
	});
	var activeTab = localStorage.getItem('activeTab');
	if(activeTab){
		$('#Tab a[href="' + activeTab + '"]').tab('show');
	}
});

function separar(arreglo){
    textarea = arreglo.toString()
    let reemplazo = textarea
    while(reemplazo.includes(',')){
        reemplazo = reemplazo.replace(',', ' ')
    }
    let reemplazo2 = reemplazo
    while(reemplazo2.includes('(')){
        reemplazo2 = reemplazo2.replace('(', ' ')
    }
    let reemplazo3 = reemplazo2
    while(reemplazo3.includes(')')){
        reemplazo3 = reemplazo3.replace(')', ' ')
    }
    let reemplazo4 = reemplazo3
    while(reemplazo4.includes('  ')){
        reemplazo4 = reemplazo4.replace('  ', ' ')
    }
    let reemplazo5 = reemplazo4
    while(reemplazo5.includes('\n')){
        reemplazo5 = reemplazo5.replace('\n', ' ')
    }

    let limpiar = reemplazo5.trim()
    let separacion = limpiar.split(' ')

    return separacion
}

function memoria(event) {
    var codigo = event.which || event.keyCode;
    if(codigo === 13){
        let str = document.getElementById("textIn").value.trim()
        num = num + 4
        let decimal = decimalAHexa(num)
        let final = str+"\n"+decimal.trim()
        $("#textIn").val(final.trim())
    }     
}


function descargar() {
    var textInput = document.getElementById("textIn").value;
    var filename = "riscV.txt";
    var element = document.createElement('a');
    element.setAttribute('href','data:text/plain;charset=utf-8,' + encodeURIComponent(textInput));
    element.setAttribute('download', filename);
    document.body.appendChild(element);
    element.click();
}


function decimalAHexa(d) { 
    var hex = d.toString(16);
    if (hex.length == 1){
        hex = "000" + hex; 
    }
    if (hex.length == 2){
        hex = '00' + hex;
    }
    if (hex.length == 3){
        hex = '0' + hex;
    }    
    return hex; 
}

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
            
            let = func3 = data[''+tipo+'']['func3']
            let = func7 = data[''+tipo+'']['func7']
            let = opcode = data[''+tipo+'']['opcode']
            let = rs1 = data[''+tipo+'']['rs1']
            let = rs2 = data[''+tipo+'']['rs2']
            let = rd = data[''+tipo+'']['rd']
            
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
            
            let = func3 = data[''+tipo+'']['func3']
            let = opcode = data[''+tipo+'']['opcode']
            let = rs1 = data[''+tipo+'']['rs1']
            let = inm = data[''+tipo+'']['inmediato']
            let = rd = data[''+tipo+'']['rd']
            
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
            
            let = func3 = data[''+tipo+'']['func3']
            let = opcode = data[''+tipo+'']['opcode']
            let = rs1 = data[''+tipo+'']['rs1']
            let = inm = data[''+tipo+'']['inmediato']
            let = rd = data[''+tipo+'']['rd']
            
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
    let rs1 = str[2]// rs1
    let inm = str[3]// inm
    let rs2 = str[4]// rs2
    let traduccion = ''
    $.ajax({
        async: false,
        url: '/'+tipo+'',
        type: 'GET',
        data:  {'inm':inm,'rs1':rs1,"rs2":rs2},
        success: function(data){
            
            let = func3 = data[''+tipo+'']['func3']
            let = opcode = data[''+tipo+'']['opcode']
            let = rs1 = data[''+tipo+'']['rs1']
            let = inm5 = data[''+tipo+'']['inmediato5']
            let = inm7 = data[''+tipo+'']['inmediato7']
            let = rs2 = data[''+tipo+'']['rs2']
            
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
            
            let = hexa = data[''+tipo+'']['hexa']
            let = rs1 = data[''+tipo+'']['rs1']
            let = ceros10 = data[''+tipo+'']['ceros10']
            let = ceros11 = data[''+tipo+'']['ceros11']
            
            traduccion = ceros11+rs1+ceros10+hexa
        },
        error: function(error){
            console.log('error: '+error)
        }
    })
    return traduccion
}

function traducir(){
    let lin = document.getElementById("textIn").value
    let linea = lin.split("\n")
    let resp = ''
    let val2 = ''
    let val3 = ''
    let val4 = ''
    let valIns = ''
    document.getElementById('LabelError').innerHTML=""
    $("#textOut").val('')
    for (let i=0; i < linea.length; i++){     
        lineaL = separar(linea[i])
        resp = ''
        val2 = ''
        val3 = ''
        val4 = ''
        valIns = ''
        if(lineaL.length > 1){
            const InstruccionesTipoR = ['add','sub','sll','slt','sltu','xor','srl','sra','or','and']
            const InstruccionesTipoI = ['addi','andi','ori','xori','slti','sltiu','slli','srli','srai']
            const InstruccionesTipoLoadI = ['lb','lh','lw','lbu','lhu']
            const InstruccionesTipoStorageS = ['sb','sh','sw']
            const InstruccionesTipoHexadecimales = ['shot','reti']
            const InstruccionTipoPTO = ['pto']

            let strr = document.getElementById("textOut").value.trim()
            let errores = document.getElementById('LabelError').innerHTML
                    
            if(InstruccionesTipoR.includes(lineaL[1])){
                val2 = validarPuntero(lineaL[2],'rd')
                val3 = validarPuntero(lineaL[3],'rs1')
                val4 = validarPuntero(lineaL[4],'rs2')
                resp = traducirTipoR(lineaL)
            }else if(InstruccionesTipoI.includes(lineaL[1])){
                val2 = validarPuntero(lineaL[2],'rd')
                val3 = validarPuntero(lineaL[3],'rs1')
                val4 = validarConstante(lineaL[4])
                resp = traducirTipoI(lineaL)
            }else if(InstruccionesTipoLoadI.includes(lineaL[1])){
                val2 = validarPuntero(lineaL[2],'rd')
                val3 = validarConstante(lineaL[3])
                val4 = validarPuntero(lineaL[4],'rs1')
                resp = traducirTipoLoadI(lineaL)
            }else if(InstruccionesTipoStorageS.includes(lineaL[1])){
                val2 = validarPuntero(lineaL[2],'rs1')
                val3 = validarConstante(lineaL[3])
                val4 = validarPuntero(lineaL[4],'rs2')
                resp = traducirTipoStoreS(lineaL)
            }else if(InstruccionesTipoHexadecimales.includes(lineaL[1])){
                resp = traducirTiposHexadecimales(lineaL)
            }else if(InstruccionTipoPTO.includes(lineaL[1])){
                val2 = validarPuntero(lineaL[2],'rs1')
                val3 = validarHexadecimal(lineaL[3])
                resp = traducirTipoPTO(lineaL)
            }else{
                valIns = validarInstruccion(lineaL)
            }
            $("#textOut").val(strr+'\n'+resp.trim())

            if(val2.length > 0 || val3.length > 0 || val4.length > 0 || valIns.length > 0){
                document.getElementById('LabelError').innerHTML=errores+'<br>Errores en la posici&oacute;n de memoria: '+lineaL[0]+''+valIns+''+val2+''+val3+''+val4;
            }
        }   
    }
}