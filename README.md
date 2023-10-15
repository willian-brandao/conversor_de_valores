# conversor_de_valores
Sistema para converter valores decimais em binários, octais e hexadecimais.

binario.py - Primeiro módulo criado converte um número decimal, ex: 2 em um número binário: 10;
Esse módulo recebe um número natural inteiro como parametro. Logo depois é criada uma lista vazia que recebe o resto a divisão 2 toda vez que esse número passa pelo laço de repetição, logo após o número inteiro é dividido por dois.
No final do módulo essa lista é percorrida de forma decrescente e armazenada em uma string que é retornada para o módulo principal.

octal.py - O segundo módulo criado converte um número decimal em formato octal. O número inserido nesse caso recebe o resto da divisão por 8 e é dividido por 8 cada vez que passa pelo laço de repetição.

hexadecimal.py - O terceiro módulo criado converte um número decimal em formato hexadecimal. Neste caso, ao entrar no laço de repetição o resultado será o resto da divisão por 16 do numero inserido, além disso esse resultado depende de um array auxiliar que retornarão outros valores que não somente os númericos.ex:
A = 10
B = 11
C = 12
D = 13
E = 14
f = F
