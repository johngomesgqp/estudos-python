
# Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor a seu antecessor.

numero: int = int(input('Digite um número: '))

antecessor: int = numero - 1
sucessor: int = numero + 1

print(f'O número digitado foi: {numero}. \n e seu antecessor é: {antecessor} \n e seu sucessor é: {sucessor}')

# Crie um algoritmo que leia um número a mostra o seu dobro, seu triplo a raiz quadrada.

numero: float = float(input('Digite um número: '))

dobro: float = numero * 2
triplo: float = numero * 3
raiz_quadrada: float = numero ** (1/2)

print(f'O número digitado foi: {numero}. \n Seu dobro é: {dobro}. \n Seu triplo é: {triplo}. \n E sua raiz quadrada é: {raiz_quadrada}')


# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nota_01: float = float(input('Digite sua primeira nota: '))
nota_02: float = float(input('Digite sua segunda nota: '))

media: float = (nota_01 + nota_02)/2

print(f'Sua média entre as notas é: {media}')

# Escrava um programa que leia um valor em metros e exiba convertido em centímetros e milímetros.

metros: float = float(input('Digite um valor em metros: '))

centimetros: float = metros * 100
milimetros: float = metros * 1000

print(f"A distância passada em metros foi: {metros}.\nEm centimetros ela fica: {centimetros}.\nEm milimetros ela fica: {milimetros}")

# Faça um programa que leia um número inteiro qualquer e mostre sua na tela sua tabuada.

numero: int = int(input('Digite um número inteiro: '))

print('A tabuada de multiplicação desse número é:\n',numero,'x 0 =',numero * 0,'\n'
      ,numero,'x 1 =',numero * 1,'\n'
      ,numero,'x 2 =',numero * 2,'\n'
      ,numero,'x 3 =',numero * 3,'\n'
      ,numero,'x 4 =',numero * 4,'\n'
      ,numero,'x 5 =',numero * 5,'\n'
      ,numero,'x 6 =',numero * 6,'\n'
      ,numero,'x 7 =',numero * 7,'\n'
      ,numero,'x 8 =',numero * 8,'\n'
      ,numero,'x 9 =',numero * 9,'\n'
      ,numero,'x 10 =',numero * 10,'\n')


#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar. 
# Considere US$1.00 = R$5.12 (usar preço atual do dolar) 

valor_carteira: float = float(input('Digite o seu valor em carteira: '))

comprar_dolar: float = valor_carteira / 5.12

print(f'Você tem R$ {valor_carteira} em reias.\nPode comprar $ {comprar_dolar:.2f} dolar(es)')
 


# faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a 
# quantidade de tinta necessária para pintá-la sabendo que a cada litro de tinta, pinta uma área de 2m**2

largura: float = float(input('Digite a largura da parade em metros: '))
altura: float = float (input('Digite a altura da parede metros: '))

area_parede: float = largura * altura
# Dividimos por 2 porque cada litro cobre 2 metros quadrados
qtd_tinta: float  = area_parede / 2

print('Quantidade de tinta a ser utilizada é: {:.2f}'.format(qtd_tinta))

 # Faça um algoritmo que leia o preço de um produto a mostre seu novo preço. com 5% da desconto.

preco_produto: float = float(input('Digite o preço do produto: '))

desconto: float = preco_produto * (5 / 100)
novo_preco: float = preco_produto - desconto

print('O preço desse produto com desconto de 5% é: ', novo_preco)

#Faça um algoritmo que leia o salario de funcionaria e mostre seu novo salario com 15% de aumento 

valor_salario: float = float(input('Digite o valor do seu sálario: '))

aumento: float = valor_salario * (15 / 100)

novo_salario: float = valor_salario + aumento

print('Seu salario com aumento de 15% é: {:.2f}'.format(novo_salario))

