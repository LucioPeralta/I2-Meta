var first_time = true
var lista_audio;
var lista_video;

function updateSelect(opcionSeleccionada) {
    if (first_time == true) {
        let select = document.getElementById("quality_hidden");
        valores = select.value.trim()
        lista_audio = valores.split(/\s+/)
        lista_video = obtenerValoresSelect()

        first_time = false
    }

    lista = []
    if (opcionSeleccionada == "video") {
        lista = lista_video
    } else {
        lista = lista_audio
    }

    let select = document.getElementById("quality")
    select.innerHTML = ""

    for (let i = 0; i < lista.length; i++) {
        var opcion = document.createElement("option");
        opcion.value = lista[i];
        opcion.text = lista[i];
        select.appendChild(opcion);
    }
}

function obtenerValoresSelect() {
    var select = document.getElementById("quality");
    var opciones = select.options;
    var valores = [];
  
    for (var i = 0; i < opciones.length; i++) {
        valores.push(opciones[i].value);
    }
    return valores;
  }
  
