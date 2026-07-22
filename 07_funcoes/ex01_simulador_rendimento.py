"""
Jornada Girino Python - Exercício 01 (Módulo: Funções)

Objetivo:
    Desenvolver a função principal de um simulador de investimentos para 
    uma Fintech, aplicando juros compostos mensais e bônus anuais.
    Utilizando a estrutura de repetição WHILE.

Conceitos praticados:
    - Definição de funções com def
    - Estruturas de repetição com while
    - Estruturas condicionais (if)
    - Formatação de strings com f-strings
    - Operador de módulo (%)    
"""

def simular_investimento(aporte_mensal: float, taxa_juros_mensal: float, meses: int) -> float:

    """
   Simula o rendimento mensal de um investimento com bônus a cada 12 meses.

    Args:
        aporte_mensal: Valor financeiro adicionado mensalmente.
        taxa_juros_mensal: Taxa de juros aplicada ao mês (ex: 0.01 para 1%).
        meses: Tempo de duração do investimento em meses.

    Returns:
       Saldo final acumulado ao término do período.
    """    
    saldo_total: float = 0
    mes_atual: int = 1  # Contador inicia a contagem de meses no mês 1
    
    # O While vai funcionar enquanto o mes_atual for menor ou igual ao total de meses pedido
    while mes_atual <= meses:
        # Atualizando o saldo_total somando com o aporte_mensal aplicado
        saldo_total = saldo_total + aporte_mensal
        
        # Aplica a taxa_juros_mensal sobre o novo total
        saldo_total = saldo_total + (saldo_total * taxa_juros_mensal)
        
        # Calcula se chegou a 12 meses e adiciona R$ 100 de bônus
        if mes_atual % 12 == 0:
            saldo_total = saldo_total + 100
            
        # Segue com o laço de repetição avançando para o proximo mês 
        mes_atual = mes_atual + 1
            
    # Retorna o saldo final (float) ao término do período
    return saldo_total

# Mostrar a informação na tela 
print('=' * 30)
print(' SIMULADOR FINTECH ')
print('=' * 30)

# Chamamos a função passando os valores para seu parâmetros (aporte_mensal: float, taxa_juros_mensal: float, meses: int)
# que aguarda o valor retornar como 'float' 
# Variável guarada o valor para poder ser usado, a função é chamada e atribuida valores (argumentos)
saldo_final_cliente: float = simular_investimento(500, 0.01, 2) 

# Print apenas para exibir o resultado
print(f"Saldo final em conta: R$ {saldo_final_cliente:.2f}")

