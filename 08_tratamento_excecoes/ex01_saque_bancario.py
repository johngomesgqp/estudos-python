
"""
Jornada Girino Python - Exercício 01 (Módulo: Tratamento de Exceções)

Objetivo:
    Criar uma função de saque bancário que valide as operações lançando 
    exceções manuais com raise e trate os erros caso o usuário digite
    algo fora do padrão do que possa ser executado pelo programa.

Conceitos praticados:
    - Criação de funções com validações estritas
    - Lançamento de erros com raise ValueError
    - Tratamento de exceções com blocos try/except/finally
"""


def sacar(valor: float , saldo: float) -> float:

    """
        Verifica se as informações digitadas pelo usuário é diferente
        do que o sistema pode executar e e dispara exceções para proteção.

        Args:
            valor: Valor solicitado a ser sacado.
            saldo: Valor que está em conta.

        Returuns:
            float: Novo saldo calculado caso passe pelas validações.
            Raises: ValueError: Erro caso o valor seja menor/igual a zero ou maior que o saldo.       
    """ 
    
    # Tratamento de regras de negócio com lançamento de exceções
    if valor <= 0:
      raise ValueError('Valor do saque deve ser maior que zero!')
    if valor > saldo:
      raise ValueError('Saldo insuficiente!')

    return saldo - valor

# valor do saldo inicial
saldo_atual: float = 1000.00

# Inicio do tratamento dos dados para sua validação.
try:
  print('Saldo atual: ', saldo_atual)
  valor_saque: float = float(input('Digite valor do saque: '))

# Atualiza a variável saldo_atual com o retorno seguro da função
  saldo_atual: float = sacar(valor_saque, saldo_atual)

  print('Saque realizado com sucesso!')
  print(f'Saldo atual: {saldo_atual:.2f}')

except ValueError as erro:
# Captura tanto o erro de saldo/valor quanto se o usuário digitar letras!
  print(f'Erro: {erro}')

#Inclusão do bloco 'finally' para informar que o sistema finalizou
finally:
    print('Operação finalizada.')


