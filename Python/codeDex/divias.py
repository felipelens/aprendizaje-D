import math

def raiz():
    print('escribe los chinos: ')
    chi = int(input())
    print('escribe los japones: ')
    ja = int(input())
    print('escribe coreano ')
    co = int(input())
    
    chi = chi / 6.79
    ja = ja / 132.63
    co = co / 1260.94
    
    usd = chi + ja + co
    
    print(usd)

raiz()