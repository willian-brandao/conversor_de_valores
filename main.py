
import binario 
import octal

def main():
    num = int(input("digite um numero: "))
    
    #chamada da função de binário
    decBin = binario.decimal_para_binario(num)
    #chamada da função de octal
    decOctal = octal.decimal_para_octal(num)
    #chamada da função de hexadecimal
 
    print(f"O numero {num} em binario: {decBin}.")
    print(f"O numero {num} Em Octal: {decOctal}.\n")

