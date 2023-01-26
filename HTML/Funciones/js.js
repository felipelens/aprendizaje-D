
function op() {
    let num1 =  parseInt(document.getElementById('num1').value) 
    let num2 =  parseInt(document.getElementById('num2').value) 


    let resultado = num1 + num2;

    let texto = document.createElement('p')
    texto.innerHTML = "el resultado es: " + resultado;
    document.getElementById('textox').appendChild(texto);
    
}



var result = document.getElementById("enviar")
    result.addEventListener("click",op)

