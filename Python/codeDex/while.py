num = int(input('ingresa un numero del 1 al 10\nrecuerda que solo tienes 3 oportunidades: '))
num2 = 0

while num != 8 or num2 > 3:
    print(num2)
    num = int(input('No adivinaste escribe de nuevo un numero: '))
    
    if num != 8:
        num2 = num2 + 1
    
    print(num2)
    
print('adivinaste el numero')

def nueva_forma():
    num = int(input('ingresa un numero del 1 al 10\nrecuerda que solo tienes 3 oportunidades: '))
    num2 = 1
    while num != 8:
        if num2 > 2:
         break 
    print(f'llevas {num2} intentos')
    num = int(input('No adivinaste escribe de nuevo un numero: '))  
    if num != 8:
        num2 = num2 + 1         
    if num == 8:
        print('adivinaste el numero')
    else:
        print('se te acabaron los intentos')