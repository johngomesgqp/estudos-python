#Crie uma função que receba uma idade e retorne True se for maior ou igual a 18, e False caso contrário.

def maior_idade (idade: int)-> bool:
    if idade >= 18:
        return True
    else:
        return False

resultado: bool = maior_idade(10)

print(resultado)

