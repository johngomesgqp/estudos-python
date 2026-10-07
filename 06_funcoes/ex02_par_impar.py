#Par ou Ímpar: Crie uma função que receba um número inteiro e retorne a string "Par" ou "Ímpar".

def par_impar (numero: int)-> str:
    if numero % 2 == 0:
        return 'Par'
    else:
        return 'Ímpar'

resultado: str = par_impar(10)

print(resultado)
    