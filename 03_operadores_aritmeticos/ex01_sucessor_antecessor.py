"""
Jornada Girino Python - Exercício 01

Objetivo:
    Solicitar um número inteiro ao usuário e mostrar na tela o número sucessor e antecessor.
    Exibe a validação e o aviso de erro caso tenha sido digitado algo que não seja número.

Conceitos praticados:
    - Entrada de dados com input()
    - Conversão de tipos (Casting) com int
    - Formatação de strings com f-string
    - Utilização de calculo de adição, subtração e método .is()
"""

print('=' * 30)
print('Número Antecessor e Sucessor ')
print('=' * 30)

# Entrada de dados com texto para proteção
entrada_usuario: str = input('Digite um número inteiro: ').strip()

# Validação se é numérico
eh_numero: bool = entrada_usuario.isnumeric()

print('=' * 30)
# Mensagem de aviso se não for um número
print('Aviso: Você digitou um texto inválido!' * (not eh_numero))
print('=' * 30)

# Se a variável 'eh_numero' for false (0), o que foi digitado será multiplicado para evitar erro

numero: int = int(entrada_usuario) * eh_numero

# Calculo para saber qo número antecessor e sucessor
# Se a variável 'eh_numero' for true (1), ele será multiplicado pelo número que foi encontrado.
# Se for número converte para int, se for texto recebe 0 para não quebrar o código
antecessor: int = (numero - 1) * eh_numero
sucessor: int = (numero + 1) * eh_numero

# Se eh_numero for True (1), a linha é impressa normalmente.
# Se eh_numero for False (0), a linha é multiplicada por 0 e não mostra NADA!

print(f'O número digitado foi: {numero}' * eh_numero)
print(f'E seu antecessor é: {antecessor}' * eh_numero)
print(f'E seu sucessor é: {sucessor}' * eh_numero)


# Observação final: O código funciona porém junto com a mensagem de aviso ele mostra o erro 'ValueErro'
# quando digitado outras coisas que não seja números inteiros.