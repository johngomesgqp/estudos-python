"""

Jornada Girino Python - Exercício 03

Objetivo:
    Criar um sistema de cadastro simples que receba difernetes tipos de dados
    do usuário, aplique boas práticas de Type Hints, realize o tratamento correto
    de string e exiba as informações formatadas na tela.

Conceitos praticados:
    - Entrada e saída de dados com input e print
    - Conversão de tipos (Casting) com int(), float() e bool()
    - Uso de métodos de string .strip() e .upper()
    - Documentação com Type Hints: :str, : int, :float e : bool

"""

print('\n' + '='*30)
print('       SISTEMA DE CADASTRO SIMPLES       ')
print('='*30)


# Pegando dados do úsuario apenas com tipos primitivos
nome: str = input('Digite o seu primeiro nome: ')
sobrenome: str = input('Digite o seu sobrenome: ')
idade: int = int(input('Digite sua idade: '))
peso: float = float(input('Digite o seu peso: '))
cadastro_ativo: bool = input('Seu cadastro está ativo? (S/N)').strip().upper() == 'S'

#Exibindo os dados digitado
print('\n' + '='*30)
print('    Confirmação de Dados     ')
print('_'*30)
print(f'Nome Completo: {nome} {sobrenome}')
print(f'Idade........: {idade} anos')
print(f'Peso.........: {peso} kg')
print(f'Status Ativo.: {cadastro_ativo}')
print('-'*30)