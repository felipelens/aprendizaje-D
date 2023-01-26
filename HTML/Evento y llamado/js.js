function idk() {
    var nombre = document.getElementById('nombre').value;
    var edad1 = document.getElementById('edad1').value;
    var edad2 = document.getElementById('edad2').value;
    var edad3 = document.getElementById('edad3').value;

    if (document.getElementById("edad1").checked){
        alert("Elegiste ser menor de edad");
        document.getElementById("cambioNombre").innerHTML = nombre;
        document.getElementById("cambioEdad").innerHTML = edad1;
    }else if(document.getElementById("edad2").checked){
        alert("Elegiste ser adolecente ");
        document.getElementById("cambioNombre").innerHTML = nombre;
        document.getElementById("cambioEdad").innerHTML = edad2;
    }else if(document.getElementById("edad3").checked){
        alert("Elegiste ser mayor de edad");
        document.getElementById("cambioNombre").innerHTML = nombre;
        document.getElementById("cambioEdad").innerHTML = edad3;
    }

    var info = document.createElement("p");
    info.innerHTML = "En realidad esa es tu edad?";
    document.getElementById("textoNuevo").appendChild (info);
    
}


var boton = document.getElementById("eleccion");
boton.addEventListener("click", idk);   