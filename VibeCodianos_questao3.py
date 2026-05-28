# Equipe resolutora: Expressos Vermelhos de Monty
# Integrantes: Aline, Denzel, Lay e Stefano

# Questão 3 — Simulador de um Pagamento
# Equipe autora: VibeCodianos

# O programa deve ser executado em um laço de repetição `while`.

# João deseja efetuar um pagamento de uma conta, com as seguintes opções:
# - 1: À vista dinheiro com 10% de desconto.
# - 2: À vista no cartão com 5% de desconto.
# - 3: Até 2 parcelas no cartão sem desconto.
# - 4: 3 parcelas ou mais com 20% de juros do total da compra.

# Regra:O usuário deve escolher uma dessas opções, e deve aparecer o valor final a ser calculado, dependendo da situação. Se o usuário digitar o número 0 nas opções, encerre o programa.

# O programa deve pedir o preço da compra.

while True:

    valor_da_compra = float(input("Digite o valor das compras: R$ "))

    print("""
          
        ESCOLHA UMA OPÇÃO DE PAGAMENTO:
        
        1 - À VISTA DINHEIRO
        2 - À VISTA NO CARTÃO 
        3 - PARCELADO NO CARTÃO ATE 2X
        4 - PARCELADO NO CARTÃO 3X OU MAIS
          
        0  - SAIR 
        """)

    opcao = input("DÍGITE A OPÇÃO DESEJADA: ")
    
    total = 0
    desconto = 0
    
    if opcao == 1:
        desconto = 10
        desconto = valor_da_compra * 0.1
        total = valor_da_compra - (desconto)
        mens_op = "Pagamento à vista. Desconto de 10% aplicado."
    
    elif opcao == 2:
        desconto = 5
        desconto = valor_da_compra * 0.05
        total = valor_da_compra - (desconto)
        mens_op = "Pagamento à vista no cartão. Desconto de 5% aplicado."
    
    elif opcao == 3:
        desconto = 0
        valor_da_compra = total
        qtd_parcelas = total/2
        msg_op = "Compra parcelada em 2x."
    
    elif opcao == 4:
        qtd_parcelas = int(input("Escolha a quantidade de parcelas: "))
        total = valor_da_compra + (valor_da_compra * 20 / 100)
        parcela = total / qtd_parcelas
        desconto = 0
        print(f"Compra parcelada em {qtd_parcelas}x.")
        
    elif opcao == 0:
        print("O PROGRAMA SERÁ ENCERRADO!")
        break
        
    print(f"Sua compra foi no valor de R$ {valor_da_compra:.2f}, ficará por R$ {total:.2f} e seu desconto será de R$ {desconto}%.")    