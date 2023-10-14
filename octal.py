from numpy import*
import numpy as np



def decimal_para_octal(numero):
    
    num = []
    a = ''
    cont = 0
    while numero > 0:
        num.append(numero % 8)
        numero //= 8
        cont += 1
        
    for i in range( cont -1, -1, -1):
        a += str(num[i])
    return a

