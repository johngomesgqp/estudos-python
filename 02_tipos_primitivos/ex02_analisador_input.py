"""

Jornada Girino Python - Exercício 02

Objetivo
    Faça um programa que leia algo pelo teclado e mostre na tela o seu
    tipo primitivo e todas as informações possíveis sobre ele.

Conceitos praticados:
    - Entrada de dados com input()
    - Identificação de tipos com type()
    - Métodos de validação de string (.is)
    - Formatação de strings (f-strings)
"""

# Entrada de dados (será com string digitada pelo teclado para permitir as validações)
dado = input('Digite algo:')

print('\n' + '='*30)
print('     ANALISANDO O DADO      ')
print('='*30)

# Exibindo o tipo primitivo padrão do input
print(f'O tipo primitivo desse valor é: {type(dado)}')

# Validação de todas as informações possíveis sobre o dado informado
print(f'Só tem espaço? ...........................: {dado.isspace()}')
print(f'É um número? .............................: {dado.isnumeric()}')
print(f'É alfabético (só letras)? ................: {dado.isalpha()}')
print(f'É alfanumérico (letras e/ou números)? ....: {dado.isalnum()}')
print(f'É totalmente maiúsculos? .................: {dado.isupper()}')
print(f'É totalmente minúsculas? .................: {dado.islower()}')
print(f'Possui iniciais maiúsculas(capitalizado)? : {dado.istitle()}')