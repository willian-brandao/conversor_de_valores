from numpy import*
import numpy as np

from main import*

def decimal_para_binario(numero):
#criando uma lista vazia que irá armazenar os resultados de resto 0 ou 1 das divisões feitas
    num = []
#criando uma string vazia que vai receber a string
    lista = ''
#criando uma contador para inclementar o laço de repetição 
    cont = 0
#laço de repetição onde será feita a divisão do número recebido até ele chegar a 0 ou 1
    while numero > 0:
#a variavel num recebe o resto da divisão do numero que será fornecido
        num.append(numero % 2)
#divisão do numero fornecido
        numero //= 2
        cont += 1
#este laço de repetição irá percorrer a lista e converter em uma string
#obs: os valores serão percorridos em ordem decrescente
    for i in range( cont -1, -1, -1):
        lista += str(num[i])
    return lista

main()