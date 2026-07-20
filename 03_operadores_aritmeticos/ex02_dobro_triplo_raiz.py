"""
Jornada Girino Python - Exercício 02

Objetivo:
    Solicitar um número inteiro ao usuário e mostrar o seu dobro, triplo e sua raiz quadrada.

Conceitos praticados:
    - Entrada de dados com input()
    - Conversão de tipos (Casting) com int ()
    - Formatação de string com .format()
    - Utilização de calculo de multiplicação e potência
"""

print('=' * 30)
print('Dobro - Triplo - Raiz Quadrada')
print('=' * 30)

# Entrada de dados com conversão para um tipo inteiro.
numero: int = int(input('Digite um número: '))

# Calculo para saber o dobro, triplo e raiz quadrada
dobro: int = numero * 2
triplo: int = numero * 3
raiz_quadrada: float = numero ** (1/2)
# Exibição dos resultados formatados (usando .format())
print('O número digitado foi: {}. \nE o seu dobro é: {}. \nO seu triplo é: {}. \nE sua raíz é:{:.1f}'.format(numero, dobro, triplo, raiz_quadrada))