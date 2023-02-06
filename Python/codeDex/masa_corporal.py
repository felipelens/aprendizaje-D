def imc():
    print('por favor escribe su peso en kg')
    masa = float(input())
    print('por favor escribe su altura')
    altura = float(input())
    
    imc = (masa / (altura**2))
    
    print('tu IMC es de ' , imc)

imc()