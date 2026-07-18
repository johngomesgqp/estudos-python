
"""
Jornada Girino Python - Exercício 01

Objetivo:
    Solicitar dois números inteiros ao usuário, realizar a conversão
    correta dos tipos de dados e exibir a soma matemática entre eles.

Conceitos praticados:
    - Entrada de dados com input()
    - Conversão de tipos (Casting) com int()
    - Formatação de strings com .format()
"""

# Entrada de dados com (com coversão para inteiro)
numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite mais um número: '))

# Processamento (soma matemática)
soma =  numero1 + numero2

# Saída de dados (usando formatação de texto)
print('A soma entre os número {} e {} vale: {}'.format(numero1, numero2, soma))