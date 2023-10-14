# conversor_de_valores
Sistema para converter valores decimais em binários, octais e hexadecimais.

1 - Primeiro módulo criado converte um número decimal, ex: 2 em um número binário: 10;
Esse módulo recebe um número natural inteiro como parametro. Logo depois é criada uma lista vazia que recebe o resto a divisão 2 toda vez que esse número passa pelo laço de repetição, logo após o número inteiro é dividido por dois para que o valor inserido seja decrescido. 
No final do módulo essa lista é percorrida de forma decrescente e armazenada em uma string que é retornada para o módulo principal.