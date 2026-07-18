"""
Jornada Girino Python - Tipos Primitivos

O Python possui diversos tipos de dados, mas os 4 mais básicos
e fundamentais (chamados de tipos primitivos) são:

1. int   -> Números inteiros (ex: 1, 10, -5, 0)
2. float -> Números reais / de ponto flutuante (ex: 1.5, -3.14, 0.0)
3. bool  -> Valores lógicos / booleanos (True ou False)
4. str   -> Caracteres / strings / textos (ex: 'Olá Mundo', 'Python')
"""

# =============================================================================
# CASO DE ESTUDO: O problema da concatenação
# =============================================================================

# Solicitando dados ao usuário
numero1 = input('Digite um número: ')
numero2 = input('Digite mais um número: ')

# Realizando a operação
soma = numero1 + numero2

# Exibindo o resultado
print('A soma errada vale:', soma)

# EXPLICAÇÃO DO ERRO:
# O código acima não funciona perfeitamente para somar números. O sinal de '+' 
# está juntando as informações (concatenando) dentro da variável 'soma'.
# Isso acontece porque, no Python, toda informação recebida pelo teclado através
# da função input() é considerada estritamente como texto (string).

# =============================================================================
# SOLUÇÃO: Conversão de Tipos (Casting)
# =============================================================================

# Para corrigir esse comportamento, usamos um tipo primitivo antes do input.
# Isso informa ao Python que o dado recebido deve ser convertido imediatamente.

num_correto1 = int(input('Digite um número: '))
num_correto2 = int(input('Digite mais um número: '))

soma_correta = num_correto1 + num_correto2

print('A soma correta vale:', soma_correta)

# EXPLICAÇÃO DA SOLUÇÃO:
# No exemplo 'int(input())', tudo o que for digitado pelo usuário será capturado 
# pelo input() e transformado em um número inteiro (int) antes de ser guardado 
# na variável. Agora a matemática funciona de verdade!

# =============================================================================
# IDENTIFICAÇÃO: Descobrindo o tipo de dado de uma variável
# =============================================================================

# Para descobrir a qual tipo primitivo uma variável pertence, podemos passar 
# a variável dentro da função nativa type() combinada com a função print().

# Exemplo:
teste_tipo1 = input('Digite qualquer coisa para testar o tipo: ')
print(type(teste_tipo1))

# EXPLICAÇÃO DO RETORNO:
# Ao executar o código acima, o terminal vai mostrar algo como <class 'str'>. 
# Isso confirma visualmente que, por padrão, o input() sempre salva os dados 
# como formato de texto (string).

# Exemplo 2: Com conversão de tipo (Casting)
teste_tipo2 = int(input("Digite qualquer número inteiro: "))
print(type(teste_tipo2))

# EXPLICAÇÃO DO RETORNO:
# Ao executar o código acima, o terminal vai mostrar algo como <class 'int'> 
# (desde que o usuário realmente digite um número inteiro). 
# Isso confirma visualmente que podemos forçar o input() a transformar a 
# informação recebida no tipo de dado que o nosso programa precisa.