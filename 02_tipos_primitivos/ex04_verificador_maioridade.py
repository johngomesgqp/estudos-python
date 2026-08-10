"""
Jornada Girino Python - Exercício 04

Objetivo:
    Criar um sistema que verifique se a idade passada pelo usuário
    é maior de idade ou não.

Conceitos praticados:
    - Entrada e saída de dados com input e print
    - Conversão de tipos (Casting) com int()
    - Operações aritméticas básicas
    - Operadores de comparação (>=)
    - Utilização de valores lógico bool()
"""


print('\n' + '=' * 30)
print('   Verificação de maior idade   ')
print('\n' + '=' * 30)

# Pega a informação da idade digitada pelo usuário
idade: int = int(input('Digite sua idade: '))

# Faz a verificação se é verdadeiro ou falso
# Em operações matemáticas, True vale 1 e False vale 0 (e vice-versa)

maior_idade: bool = idade >= 18 # se for verdadeiro a variável passa a ter o valor 1(virce-versa)
menor_idade: bool = idade < 18 # se for falso a variável passa a ter o valor 0 (virce-versa)

# Verifica se as variáveis de verificação estão com os valores de 0 ou 1 e multiplica pela mensagem 
# Se a mensagem for multiplicada por 1 ela soma com a outra mensagem que vai ser multiplcada por 0
# e vai vai restar uma mensagem vazia pois todo número multilcado por 0 é 0 

# Multiplica o texto pelo valor numérico do booleano (1 ou 0)
# O texto multiplicado por 1 se mantém e o multiplicado por 0 vira uma string vazia
# Após a verificação as strings são somadas que é o que traz a mensagem. 
mensagem: str = ('Você é maior de idade!' * maior_idade) + ('Você é menor de idade!' * menor_idade)

# Mostara a mensagem que sobrou para o usuário
print(mensagem + ' E sua idade é:', idade )