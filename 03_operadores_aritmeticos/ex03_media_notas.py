"""
Jornada Girino Python - Exercício 03

Obejetivo:
    Solicitar dois números para usuário calcular e mostrar a sua média.

Conceitos prsticados:
    - Entrada de dados com input()
    - Conversão de tipo (Casting) com float()
    - Formatação de string com .format()
    - Utilização de calculos de adição e divisão com precedência
"""

print('-' * 30)
print('Calculo de média de notas')
print('-' * 30)

# Entrada de dados com conversão para um tipo numero real.
nota_01: float = float(input('Digite sua primeira nota: '))
nota_02: float = float(input('Digite sua segunda nota: '))

# Calculo para saber a média da aluno (parênteses para que seja somado primeiro)
media: float = (nota_01 + nota_02) / 2

# Exibição dos resultados formatados (usando .format())
print('As sua média entres as notas {} e {} vale: {:.1f}'.format(nota_01, nota_02, media))