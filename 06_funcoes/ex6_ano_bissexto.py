# Verificador de Ano Bissexto: Crie uma função que receba um ano e retorne True se for 
# bissexto e False se não for.

def ano_bissexto(ano: int)-> bool:
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

print(ano_bissexto (2028))
        