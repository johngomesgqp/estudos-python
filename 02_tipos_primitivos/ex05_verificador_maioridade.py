"""
Jornada Girino Python - Exercício 05

Objetivo:
    Solicitar o ano de nascimento do usuário, calcular a idade dele
    baseada no ano atual e retornar um valor boleano (bool) informando
    se ele é maior de idade (18 anos ou mais).

 Conceitos praticados:
    - Entrada de dados com (Casting) input()
    - Operações aritméticas básicas
    - Operadores de comparação (>=)
    - Formatação de strings (f-strings)
"""
print('=' * 30)
print(' VERIFICANDO MAIORIDADE ')
print('=' * 30)

# Entrada de dados com conversão para inteiro
ano_nascimento: int = int(input('Digite o ano de seu nascimento: (Ex: 2025): '))

# Calculando a idade com base no ano atual
ano_atual: int = 2026
idade: int = ano_atual - ano_nascimento

# Gera True se for maior/igual a 18, ou False se for menor
eh_maior: bool = idade >= 18

# Exibição dos resultados na tela
print('-' * 30)
print(f'Sua idade atual é: {idade} anos')
print(f'Já atingiu a maioridade?: {eh_maior}')
print('-' * 30)