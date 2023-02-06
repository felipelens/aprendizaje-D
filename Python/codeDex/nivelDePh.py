ph = int(input('escribe el nivel de ph: '))

if ph > 7:
    print('Básico')
elif ph < 7:
    print('Acido')
else:
    print('Neutro')