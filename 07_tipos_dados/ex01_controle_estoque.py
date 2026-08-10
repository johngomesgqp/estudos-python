"""
Jornada Girino Python - Exercício 01 Módulo: Tipos de Dados Compostos

Objetivo:
    Criar um sistema de gerenciamento de estoque para cadastrar itens 
    em uma lista de dicionários e filtrar produtos ativos com saldo zerado.

Conceitos praticados:
    - Manipulação de dicionários e listas (list e dict)
    - Uso do método .append() para adicionar elementos
    - Filtragem avançada com List Comprehension
    - Utilização de funções (def com parâmetros e retornos)
"""


# Criação de função que recebe a lista do estoque com o nome do produto, a
# quantidade e o status (cujo padrão deve ser True).

def adicionar_item( lista_estoque: str, nome: str, qtd: int, ativo: bool = True)-> None:

    """
    Cria um novo dicionário de produto e o adiciona na lista de estoque

    """
    novo_item = {
        'nome_produto' : nome,
        'qtd' : qtd,
        'ativo' : ativo
    }
    # Adicionando o item ao final da lista de estoque recebida
    lista_estoque.append(novo_item)


def obter_itens_pendentes (lista_estoque: str)-> str: 

    """
    Filtra e retorna produtos que estão ativos e com a quantidade zerada.
    
    """
    # Adicione o 'item' na nova lista para cada 'item' do 'lista_estoque'
    # SE o item estiver ativo 'E' a quantidade for igual a 0.

    itens_pendentes = [
        item for item in lista_estoque
        if item ['ativo'] == True and item ['qtd'] == 0
    ]

    return itens_pendentes

print('\n' + '=' * 30)
print('   Sistema de Controle de Estoque    ')
print('\n' + '=' * 30)

# Estoque fornecido
estoque = [

{"nome": "Prego", "qtd": 2, "ativo": True},
{"nome": "Martelo", "qtd": 6, "ativo": True},
{"nome": "Serrote", "qtd": 0, "ativo": False},

]

print ('Estoque inicial: ', estoque)

print('\n' + '=' * 30)
print('   Cadastro de Novo Produto    ')
print('\n' + '=' * 30)

# Passa as informações para função inicial e adiciona o item "Tinta" com 
# quantidade 0 e status ativo na lista informada
adicionar_item (estoque, nome= 'Tinta', qtd= '0', ativo=True)

# Pega as informações passada para função e filtra 
# e pegando os itens que precisam de reposição
relatorio_pendentes = obter_itens_pendentes(estoque)

print()

