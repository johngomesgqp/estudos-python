"""
Jornada Girino Python - Operadores Aritméticos

Objetivo:
    Aprender a realizar operações matemáticas no Python, desde as mais 
    comuns (soma e subtração) até as mais específicas (resto da divisão 
    e exponenciação).

O que são operadores aritméticos?
    São os símbolos que usamos para fazer cálculos matemáticos com os nossos 
    números (int e float) dentro do código.
"""

# =============================================================================
# OS 7 OPERADORES ARITMÉTICOS DO PYTHON
# =============================================================================

# 1. Adição (+)
soma: int = 5 + 3  # Resultado: 8

# 2. Subtração (-)
subtracao: int = 10 - 4  # Resultado: 6

# 3. Multiplicação (*)
multiplicacao: int = 4 * 2  # Resultado: 8

# 4. Divisão (/)
# ATENÇÃO: No Python, a divisão sempre retorna um número decimal (float)!
divisao: float = 10 / 4  # Resultado: 2.5


# =============================================================================
# OPERADORES ESPECIAIS (OS MAIS IMPORTANTES PARA APRENDER)
# =============================================================================

# 5. Divisão Inteira (//)
# Ele divide os números mas joga fora a parte decimal, pegando só o número inteiro.
divisao_inteira: int = 10 // 4  # Resultado: 2 (o 0.5 foi jogado fora)

# 6. Resto da Divisão ou Módulo (%)
# Ele não dá o resultado da divisão, ele dá apenas o que SOBROU dela.
# Muito usado para descobrir se um número é par ou ímpar!
resto: int = 10 % 4  # Resultado: 2 (porque 4 cabe 2 vezes no 10, e sobram 2)

# 7. Exponenciação ou Potência (**)
# Eleva um número à potência do outro (um número vezes ele mesmo).
potencia: int = 2 ** 3  # Resultado: 8 (que é 2 * 2 * 2)


# =============================================================================
# ORDEM DE PRECEDÊNCIA (Quem o Python resolve primeiro?)
# =============================================================================
# Assim como na matemática da escola, o Python segue uma ordem para resolver contas:
# 1º: Parênteses ( ) -> Tudo dentro deles é resolvido antes de tudo!
# 2º: Exponenciação **
# 3º: Multiplicação *, Divisão /, Divisão Inteira //, Resto % (Quem aparecer primeiro)
# 4º: Adição + e Subtração - (Quem aparecer primeiro)

# Exemplo prático da importância dos parênteses:
conta_errada: float = 5 + 5 / 2    # O Python faz 5/2 (= 2.5) e soma 5. Resultado: 7.5
conta_certa: float = (5 + 5) / 2  # O Python faz o parênteses primeiro. Resultado: 5.0

print(f"Sem parênteses: {conta_errada}")
print(f"Com parênteses: {conta_certa}")


# =============================================================================
# OUTRAS FORMAS DE FAZER CÁLCULOS (FUNÇÕES E RAÍZES)
# =============================================================================

# Usando a função interna de potência pow():
# Ao usar essa função nativa, perde-se a ordem de precedência mostrada antes.
potencia_pow = pow(4, 3)  # É o mesmo que 4 ** 3. Resultado: 64

# Descobrindo a raiz quadrada e cúbica de um número:
# Na matemática, calcular a raiz quadrada de um número é o mesmo que elevar esse 
# número à potência de meio (0.5 ou 1/2). O Python calcula os parênteses primeiro.

raiz_quadrada: float = 81 ** (1 / 2)  # Resultado: 9.0 (pois 9 * 9 = 81)

# Esse conceito serve para as demais raízes também (como a raiz cúbica):
raiz_cubica: float = 125 ** (1 / 3)  # Resultado: 5.0 (pois 5 * 5 * 5 = 125)


# =============================================================================
# OPERADORES ARITMÉTICOS COM STRINGS (TEXTOS)
# =============================================================================

# O sinal de "+" (Concatenação): junta duas strings diretamente.
mensagem_junta = 'Oi' + 'Olá'  # Resultado: 'OiOlá'

# O sinal de "*" (Replicação): repete o texto a quantidade de vezes pedida.
linha_visual = '=' * 20  # Resultado: '===================='

# Quando usamos isso dentro do print(), a string é impressa pura, sem as aspas:
print('=' * 20)


# =============================================================================
# ALINHAMENTOS E FORMATAÇÃO DE TEXTO NO PRINT
# =============================================================================

nome: str = 'Girino'

# 1. Espaçamento simples {:20} -> Reserva 20 espaços para o texto
print('Prazer em te conhecer {:20}!'.format(nome))

# 2. Alinhamento à Direita {:>20} -> Joga o texto para a direita nos 20 espaços
print('Prazer em te conhecer {:>20}!'.format(nome))

# 3. Alinhamento à Esquerda {:<20} -> Joga o texto para a esquerda (padrão)
print('Prazer em te conhecer {:<20}!'.format(nome))

# 4. Centralizado {:^20} -> Centraliza o texto nos 20 espaços
print('Prazer em te conhecer {:^20}!'.format(nome))

# 5. Centralizado com preenchimento {:=^20} -> Preenche os lados vazios com '='
print('Prazer em te conhecer {:=^20}!'.format(nome))


# =============================================================================
# CÁLCULOS DIRETOS NO PRINT E EVOLUÇÃO DO PYTHON
# =============================================================================

# HISTÓRICO: A partir do Python 3, a instrução print passou a ser uma 
# "Built-in Function" (função interna). Por isso, o uso dos parênteses () 
# tornou-se obrigatório. Nas versões antigas (Python 2), ele funcionava sem ().

# Podemos fazer cálculos direto na exibição, economizando memória:
numero1: int = int(input('Digite um valor: '))
numero2: int = int(input('Digite outro valor: '))

print('A soma vale: {}'.format(numero1 + numero2))

# REGRA DE OURO: Só faça o cálculo direto no print se NÃO for precisar usar 
# esse resultado mais adiante no código. Se precisar dele depois, use variáveis.


# =============================================================================
# CONTROLE DE LINHAS NO TERMINAL (end='' e \n)
# =============================================================================

soma = numero1 + numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2
divisao_inteira = numero1 // numero2
potencia = numero1 ** numero2

# end='' -> Evita que o print pule uma linha automaticamente. 
# O próximo print vai começar colado na mesma linha!
print('A soma é {}, a multiplicação é {}, a divisão é {:.3f} '.format(soma, multiplicacao, divisao), end='')
print('-> divisão inteira {} e potência {}'.format(divisao_inteira, potencia))

# \n -> Quebra a linha em qualquer parte do texto onde for colocado.
print('\nPrimeira linha.\nSegunda linha.')
