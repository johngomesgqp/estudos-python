"""
Jornada Girino Python - Exercício 02 

Objetivo:
    Pegar um código bagunçado cheio de erros de sintaxe e violações da PEP 8, 
    aplicar as regras corretas de nomenclatura (snake_case), adicionar 
    Type Hints e formatar a saída.

Código original problemático:
    1nome = "Girino"
    sobrenome do usuario = "Dev"
    Idade_Usuario = 18
    $salario = 1500.50
"""

print('\n' + '='*30)
print('       CÓDIGO REFATORADO (PADRÃO PEP 8)  ')
print('='*30)

# Correção dos nomes das variáveis + Adição de Type Hints
primeiro_nome: str = "Girino"
sobrenome_usuario: str = "Dev"
idade_usuario: int = 18
salario_atual: float = 1500.50

# Exibição das informações limpas e organizadas na tela
print(f"Desenvolvedor: {primeiro_nome} {sobrenome_usuario}")
print(f"Idade........: {idade_usuario} anos")
print(f"Salário Base.: R$ {salario_atual:.2f}")
