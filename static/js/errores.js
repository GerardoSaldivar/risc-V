function validarPuntero(arrP,tipo){
    const punteros = ['x0','X0','x1','X1','x2','X2','x3','X3','x4','X4','x5','X5','x6','X6','x7','X7','x8','X8','x9','X9','x10','X10','x11','X11','x12','X12','x13','X13','x14','X14','x15','X15','x16','X16','x17','X17','x18','X18','x19','X19','x20','X20','x21','X21','x22','X22','x23','X23','x24','X24','x25','X25','x26','X26','x27','X27','x28','X28','x29','X29','x30','X30','x31','X31']
    let respuesta = ''
    if (punteros.includes(arrP)){
        respuesta = ''
    }else if(arrP === undefined){
        respuesta = '<br>- No se encontro el puntero '+tipo+' '
    }else{
        respuesta = '<br>- El puntero '+tipo+' con valor '+arrP+' no es v&aacute;lido'
    }
    return respuesta
}

function validarConstante(arrC){
    let respuesta = ''
    if (arrC <= 2047 && arrC >= -2048){
        respuesta = ''
    }else if(arrC === undefined){
        respuesta = '<br>- No se encontro el decimal'
    }else{
        respuesta = '<br> - N&uacute;mero '+arrC+' fuera de rango debe ser menor a 2047 y  mayor a -2048'
    }
    return respuesta
}

function validarHexadecimal(arrH){
    console.log('tipo: '+typeof(arrH))
    let respuesta = ''
    if (arrH > 0){
        respuesta = ''
    }else if(arrH === undefined){
        respuesta = '<br>- No se encontro el hexadecimal'
    }else{
        respuesta = '<br>- No se encontro el hexadecimal'
    }
    return respuesta
}

function validarEtiqueta(arrEt){
    let respuesta = ''
    if(etiquetas.has(arrEt)){
        respuesta = ''
    }else{
        respuesta = '<br>- No se encontro la etiqueta: '+arrEt
    }
    return respuesta
}