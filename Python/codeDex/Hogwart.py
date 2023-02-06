print('===============================================================')
print('responde las siguientes preguntas para saber a cual escuela vas')
print('* Gryffindor                                                   ')
print('* Ravenclaw                                                    ')
print('* Hufflepuff                                                   ')
print('* Slytherin                                                    ')
print('===============================================================')

def preguntas():
    #variables globales
    Gryffindor = 0
    Ravenclaw = 0
    Hufflepuff = 0 
    Slytherin = 0
    
    #Seccion de primera preguntas
    print('===============================================================')
    print('te gusta amanecer o anochecer                                  ')
    print('1) amanecer                                                    ')
    print('2) anochecer                                                   ')
    print('===============================================================')
    
    #condiciones
    q1 = int(input('Tu respuesta es: '))
    if q1 == 1:
        Gryffindor += 1
        Ravenclaw += 1
    elif q1 == 2:
        Hufflepuff += 1
        Slytherin += 1
    else:
        print('el limite solo es de dos respuestas')
        
    #Seccion de segunda pregunta  
    print('===============================================================')
    print('Cuando esté muerto, quiero que la gente me recuerde como:      ')
    print('1) El Bien                                                     ')
    print('2) El Grande                                                   ')
    print('3) El Sabio                                                    ')
    print('4) El audaz                                                    ') 
    print('===============================================================')
    
    q2 = int(input('Tu respuesta es: '))
    
    #condiciones
    if q2 == 1:
        Hufflepuff += 1
    elif q2 == 2:
        Slytherin +=1
    elif q2 == 3:
        Ravenclaw +=1
    elif q2 == 4:
        Gryffindor +=1
    else:
        print('solo escribes numeros del 1 al 4')
        
    #Seccion de tercera preguntas
    print('===============================================================')
    print('¿Qué tipo de instrumento agrada más a tu oído?                 ')
    print('1) El violín                                                   ')
    print('2) La trompeta                                                 ')
    print('3) El piano                                                    ')
    print('4) El tambor                                                   ')
    print('===============================================================')
    
    q3 = int(input('Tu respuesta es: '))
    
    #condiciones
    if q3 == 1:
        Slytherin +=1
    elif q3 == 2:
        Hufflepuff +=1
    elif q3 == 3:
        Ravenclaw +=1
    elif q3 == 4:
        Gryffindor +=1
    else:
        print('solo escribes numeros del 1 al 4')
        
    print('===========================================================================')   
    
    if Gryffindor > Slytherin and Gryffindor > Hufflepuff and Gryffindor > Ravenclaw:
        print('perteneces a grifindor')
    elif    Slytherin > Hufflepuff and Slytherin > Ravenclaw:
        print('perteneces a esliterin')
    elif     Hufflepuff > Ravenclaw:
        print('eres un verdadero hafopoff')
    else:
        print(' eres un verdadero revenclou')
    
    print('===========================================================================')
    
preguntas()