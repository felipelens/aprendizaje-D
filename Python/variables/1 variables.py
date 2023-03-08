# declarar variable
nombre = "cristian "
apellido = "lenis"
edad = 21

# imprimir y concatenar con +
print(nombre+apellido)

# eliminar variable
del apellido

# concatenar con f a string
print(nombre + f"{edad}")

# forma correcta de asignar nombres a variables
nombre_completo = "cristian felipe lenis"

# para saber si existe un texto en una variable
print("felipe" in nombre_completo) # con in es para saber si esta
print("bulla" not in nombre_completo) # con not in es para saber si no esta

#type es para saber que tipo de variable es
type()