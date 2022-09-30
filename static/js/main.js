let num = 0;
const etiquetas = new Map()

const InstruccionesTipoR = ['add','sub','sll','slt','sltu','xor','srl','sra','or','and']
const InstruccionesTipoI = ['addi','andi','ori','xori','slti','sltiu','slli','srli','srai']
const InstruccionesTipoLoadI = ['lb','lh','lw','lbu','lhu']
const InstruccionesTipoStorageS = ['sb','sh','sw']
const InstruccionesTipoB = ['beq','bne','blt','bge','bltu','bgeu']
const InstruccionesTipoHexadecimales = ['shot','reti']
const InstruccionTipoPTO = ['pto']

$(document).ready(function(){
    let str = document.getElementById("textIn").value.trim()
    if(str === ""){
        $("#textIn").val('0000')
    }else{
        console.log("no vacio")
    }

    //sesion del textarea del lenguaje ensamblador
    let field = document.getElementById("textIn");
    if (sessionStorage.getItem("autosave")) {
        field.value = sessionStorage.getItem("autosave");
    }

    field.addEventListener("change", () => {
        sessionStorage.setItem("autosave", field.value);
    });
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

function buscarEtiquetas(){
    
    let lin = document.getElementById("textIn").value
    let linea = lin.split("\n")

    for (let i=0; i < linea.length; i++){
        etiqueta = separar(linea[i])

        if(esEtiqueta(etiqueta)){
            etiquetas.set(etiqueta[1],etiqueta[0])
        }
    }
}

function esEtiqueta(etiqueta){
    const total = InstruccionesTipoR.concat(InstruccionesTipoI.concat(InstruccionesTipoLoadI.concat(InstruccionesTipoStorageS.concat(InstruccionesTipoB.concat(InstruccionesTipoHexadecimales.concat(InstruccionTipoPTO))))))
    if(total.includes(etiqueta[2])){
        return true
    }else if(total.includes(etiqueta[1])){
        return false
    }
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

function HexadecimalADecimal(h){
    let number = parseInt(h, 16);
    return number;
}

function traducir(){
    buscarEtiquetas()
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

            let strr = document.getElementById("textOut").value.trim()
            let errores = document.getElementById('LabelError').innerHTML

            if(esEtiqueta(lineaL)){//si contiene una etiqueta
                if(InstruccionesTipoR.includes(lineaL[2])){
                    val2 = validarPuntero(lineaL[3],'rd')
                    val3 = validarPuntero(lineaL[4],'rs1')
                    val4 = validarPuntero(lineaL[5],'rs2')
                    resp = traducirTipoRE(lineaL)
                }else if(InstruccionesTipoI.includes(lineaL[2])){
                    val2 = validarPuntero(lineaL[3],'rd')
                    val3 = validarPuntero(lineaL[4],'rs1')
                    val4 = validarConstante(lineaL[5])
                    resp = traducirTipoIE(lineaL)
                }else if(InstruccionesTipoLoadI.includes(lineaL[2])){
                    val2 = validarPuntero(lineaL[3],'rd')
                    val3 = validarConstante(lineaL[4])
                    val4 = validarPuntero(lineaL[5],'rs1')
                    resp = traducirTipoLoadIE(lineaL)
                }else if(InstruccionesTipoStorageS.includes(lineaL[2])){
                    val2 = validarPuntero(lineaL[3],'rs1')
                    val3 = validarConstante(lineaL[4])
                    val4 = validarPuntero(lineaL[5],'rs2')
                    resp = traducirTipoStoreSE(lineaL)
                }else if(InstruccionesTipoHexadecimales.includes(lineaL[2])){
                    resp = traducirTiposHexadecimales(lineaL)
                }else if(InstruccionTipoPTO.includes(lineaL[2])){
                    val2 = validarPuntero(lineaL[3],'rs1')
                    val3 = validarHexadecimal(lineaL[4])
                    resp = traducirTipoPTOE(lineaL)
                }
            }else if(esEtiqueta(lineaL)===false){// no contiene una etiqueta
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
                }else if(InstruccionesTipoB.includes(lineaL[1])){
                    val2 = validarPuntero(lineaL[2],'rs1')
                    val3 = validarPuntero(lineaL[3],'rs2')
                    resp = traducirTipoB(lineaL)
                }else if(InstruccionesTipoHexadecimales.includes(lineaL[1])){
                    resp = traducirTiposHexadecimales(lineaL)
                }else if(InstruccionTipoPTO.includes(lineaL[1])){
                    val2 = validarPuntero(lineaL[2],'rs1')
                    val3 = validarHexadecimal(lineaL[3])
                    resp = traducirTipoPTO(lineaL)
                }
            }else{
                valIns = '<br> - Tipo de instrucci&oacute;n no v&aacute;lida'
            }
            let salida = strr+'\n'+resp
            $("#textOut").val(salida.trim())
                
            if(val2.length > 0 || val3.length > 0 || val4.length > 0 || valIns.length > 0){
                document.getElementById('LabelError').innerHTML=errores+'<br>Errores en la posici&oacute;n de memoria: '+lineaL[0]+''+valIns+''+val2+''+val3+''+val4;
            }
        }   
    }
}


/*else if(val2.length == 0 && val3.length == 0 && val4.length == 0 && valIns.length == 0){
    document.getElementById('LabelError').innerHTML='<br> ¡ Traduccion completa !'
}*/