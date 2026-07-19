"""
Jornada Girino Python - Exercício 01 

Objetivo:
    Criar duas variáveis (a e b) com valores iniciais diferentes, realizar 
    a inversão dos valores entre elas e exibir o resultado antes e depois.

Conceitos praticados:
    - Atribuição de variáveis
    - Reatribuição de valores na memória
    - Truque de atribuição múltipla do Python (a, b = b, a)
    - Exibição de dados com f-strings
"""

print('\n' + '='*30)
print('         DESAFIO: TROCA DE VALORES       ')
print('='*30)

# 1. Definição das variáveis iniciais usando Type Hints
a: int = 10
b: int = 20

print("--- Valores Iniciais ---")
print(f"Variável A vale: {a}")
print(f"Variável B vale: {b}")

# 2. Processamento: Realizando a inversão dos valores (Truque do Python)
a, b = b, a

print("\n--- Valores Após a Troca ---")
print(f"Variável A agora vale: {a} (Esperado: 20)")
print(f"Variável B agora vale: {b} (Esperado: 10)")

