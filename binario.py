from numpy import*
import numpy as np
from main import*

def decimal_para_binario(numero):
    #numero = int(input("Digite um numero:"))
    num = []
    a = ''
    cont = 0
    while numero > 0:
        num.append(numero % 2)
        numero //= 2
        cont += 1
    for i in range( cont -1, -1, -1):
        a += str(num[i])
    return a

main()