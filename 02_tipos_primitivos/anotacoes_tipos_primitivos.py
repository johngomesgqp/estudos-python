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


# =============================================================================
# VALIDAÇÃO: Verificando características de um texto com métodos .is()
# =============================================================================

# Os tipos primitivos também podem ser validados através de métodos internos da 
# string. Eles ajudam a verificar se é possível ou seguro converter o valor 
# informado para um determinado tipo primitivo.

# Alguns dos métodos mais comuns são:
# .isnumeric() -> Verifica se o texto contém apenas números.
# .isalpha()   -> Verifica se o texto contém apenas letras.
# .isalnum()   -> Verifica se o texto é alfanumérico (letras e/ou números).
# .isupper()   -> Verifica se o texto é composto apenas por letras maiúsculas.

# Exemplo:
teste_validacao = input('Digite algo para validação: ')

# O método retorna True (Verdadeiro) ou False (Falso)
print('É numérico?', teste_validacao.isnumeric())
print('É alfabético?', teste_validacao.isalpha())
print('Está tudo em maiúsculo?', teste_validacao.isupper())

# EXPLICAÇÃO DO RETORNO:
# Esses métodos são fundamentais para evitar erros no programa. Ao receber o dado 
# como texto (str), podemos rodar o .isnumeric() antes. Se o retorno for True, 
# sabemos que é 100% seguro converter essa variável para um número inteiro (int).

# =============================================================================
# TRATAMENTO: Limpeza e padronização de textos com .strip() e .upper()
# =============================================================================

# Os métodos .strip() e .upper() podem ser aplicados em qualquer texto para 
# transformar ou limpar conteúdos.

# Exemplo prático:
ativo: bool = input('O cadastro está ativo? (S/N): ').strip().upper() == 'S'

# O método .strip() -> É um limpador de espaços em branco.
# Ele remove todos os espaços invisíveis que o usuário pode ter digitado sem 
# querer antes ou depois do texto. 
# Exemplo: se digitar "  s  ", o .strip() limpa e transforma em "s". Isso evita 
# que o programa falhe por causa de um espaço acidental.

# O método .upper() -> É um conversor para letras maiúsculas.
# Ele transforma todas as letras minúsculas do texto em letras maiúsculas.
# Exemplo: se o usuário digitar "s", o .upper() transforma em "S".

# Como os dois funcionam juntos (Encadeamento de métodos):
# Eles servem para fazer uma padronização da resposta. Sem esses métodos, se o 
# usuário digitasse " s " ou "s", o programa daria o resultado como False (Inativo), 
# porque o Python entende que "s" minúsculo ou com espaços é totalmente diferente 
# de "S" maiúsculo puro.
# Ao juntar os dois (.strip().upper()), garante que não importa se o usuário 
# digitou "s", "  s  " ou "S": o Python vai limpar os espaços, transformar em 
# maiúsculo e ler apenas "S". Assim, a comparação == "S" funciona perfeitamente.


# =============================================================================
# DOCUMENTANDO O CÓDIGO: Uso de Type Hints (Dicas de Tipo)
# =============================================================================

# O Type Hint ("Dica de tipo") serve para deixar claro qual é o tipo de dado que 
# uma variável deve receber. O Python ignora o Type Hint na hora de rodar o código, 
# pois ele serve apenas para orientar o programador, seguir boas práticas e ajudar 
# o editor de código (como o VS Code) a sugerir os métodos certos para aquela variável.

# Exemplo sem Type Hint (O Python descobre o tipo sozinho):
aprendiz = 'Girino Dev'

# Exemplo com Type Hint (Você avisa ao editor e documenta o tipo da variável):
aprendiz: str = 'Girino Dev'


# ATENÇÃO / OBSERVAÇÃO IMPORTANTE:
# O Type Hint não bloqueia erros sozinho! Se você rodar o código abaixo, ele 
# vai funcionar perfeitamente e vai imprimir o texto 'Vinte e Cinco'. O Python 
# não vai parar o programa e nem gerar um erro, porque ele ignora a dica ': int'.

idade: int = 'Vinte e Cinco'
print(idade)

# Para garantir que o dado mude de tipo de verdade e evitar esse tipo de situação, 
# você deve usar a conversão real (Casting) usando int(), float(), etc., em vez 
# de apenas colocar a dica visual do Type Hint.
