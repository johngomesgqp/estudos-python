# Calculadora de IMC: Crie uma função que receba peso e altura. Retorne o valor do IMC calculado.

def calc_imc (peso: float, altura: float)-> float:
    imc: float = peso / altura ** 2
    return imc

resultado: float = calc_imc(85, 1.76)

print('Seu IMC é: {:.2f}'.format(resultado))
    