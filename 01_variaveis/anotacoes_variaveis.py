"""
Jornada Girino Python - Variáveis

Objetivo:
    Entender o conceito de variáveis, regras de nomeação baseadas 
    na PEP 8, atribuição de valores e o uso prático de Type Hints.

O que é uma variável?
    É um espaço reservado na memória do computador para armazenar dados 
    temporariamente enquanto o programa está rodando.
"""

# =============================================================================
# REGRAS DE NOMEAÇÃO (PEP 8)
# =============================================================================

# REGRA 1: Use o padrão snake_case (letras minúsculas separadas por underline).
nome_usuario: str = 'John'
idade_atual: int = 25

# REGRA 2: Nunca comece o nome de uma variável com números.
# Errado: 1_numero = 10
# Certo:
primeiro_numero: int = 10

# REGRA 3: Não use espaços em branco e evite acentos ou caracteres especiais.
# Errado: preço total = 50.0 / preco_tot@l = 50.0
# Certo:
preco_total: float = 50.0

# REGRA 4: Escolha nomes que façam sentido (seja descritivo, evite letras soltas).
# Ruim: x = 30 (o que é x?)
# Bom:
dias_do_mes: int = 30

# =============================================================================
# CONCEITO DE ATRIBUIÇÃO E REATRIBUIÇÃO
# =============================================================================

# O sinal de igual (=) significa ATRIBUIÇÃO (recebe), e não igualdade matemática.
# Lemos: "A variável 'carteira' RECEBE o valor 15.0"
carteira: float = 15.0

# Reatribuição: O valor de uma variável pode mudar ao longo do programa.
carteira = 50.75  # O valor antigo (15.0) foi apagado e substituído pelo novo.

# =============================================================================
# CONSTANTES (PEP 8)
# =============================================================================

# Se um valor NUNCA deve mudar durante o programa, usamos letras TOTALMENTE MAIÚSCULAS.
# Isso avisa a outros programadores que essa variável é uma constante.
PI: float = 3.14159
SUCESSO_HTTP: int = 200


# =============================================================================
# EXIBIÇÃO MODERNA: F-strings e Formatação Dinâmica (:.2f)
# =============================================================================

# A F-string (Formatted String) é a forma mais moderna e limpa de juntar textos 
# e variáveis em um único print(). Basta colocar a letra 'f' antes das aspas 
# e colocar a variável direto dentro de chaves {}.

produto: str = 'Mouse Gamer'
preco: float = 129.90

# Exemplo simples de F-string:
print(f'O produto {produto} custa {preco} reais.')

# O comando FILTRO DE CASAS DECIMAIS (:.2f):
# Quando trabalhamos com moedas ou notas fiscais, o Python pode exibir muitas 
# casas decimais (ex: 129.9). Para forçar o programa a mostrar apenas 2 casas 
# decimais após o ponto, usamos o código ':.2f' colado no nome da variável.

salario_girino: float = 1500.5  # O Python leria como 1500.5

# Exemplo aplicando a formatação com :.2f
print(f'O salário formatado é: R$ {salario_girino:.2f}')  # Saída: R$ 1500.50