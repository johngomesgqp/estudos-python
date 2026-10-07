#Maior de Três: Crie uma função que receba três números inteiros e retorne qual é o maior entre eles.

def maior_de_tres (numero_1: int, numero_2: int, numero_3: int )-> int:
    if numero_1 > numero_2 and numero_1 > numero_3:
        return numero_1

    elif numero_2 > numero_1 and numero_2 > numero_3:
        return numero_2
    else:
        return numero_3

maior_numero: int = maior_de_tres(5, 10, 15)

print(f'E o maior número entre eles é: {maior_numero}')