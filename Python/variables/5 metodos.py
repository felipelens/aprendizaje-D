num = 1
nombre = "Cristian Felipe"
prueba = "32132"
prueba2 = "aasdfasdf123456789"
#! Funciones
# type(variable) #* funciona para saber que tipo de dato se esta ingresando
# dir(variable) #* funciona para saber que podemos hacer con ese tipo de dato
# len(variable) #* funciona para saber cuantos caracteres hay en una varriable
#! Funciones


#! Metodos
# es una funcion aplicada a un objeto
# para poner en mayusculas
result = nombre.upper() 

# para poner en minusculas
result = nombre.lower() 

# primera letra en mayusculas
result = nombre.capitalize() 

# para buscar un string en alguna cadena y que devuelva la posicion en numero
result = nombre.find("e") 

# index funciona igual que find() pero si no encuentra la letra a buscar depura una exepcion
result = nombre.index("e")

# si es numerico devuelve true
result = prueba.isnumeric()

# si es alfanumerico devuelve true a hasta z
result = prueba2.isalpha()


# count funciona para saber cuantos letras estan repetidas en una variable
# si no encuentra nada devuelve 0
result = nombre.count("e")

# si empieza con " " devuelve true
result = nombre.startswith("Cri")

# si termina con " " devuelve true
result = nombre.endswith("e")

#reemplaza dentro de una cadena
#si encuentra la coincidencia
result = nombre.replace("Felipe","lenis")

#es capaz de seperar cadenas y volverla una lista
#toca darle que dato va sperar ""
result = nombre.split(" ")


#! Metodos

print(result)




