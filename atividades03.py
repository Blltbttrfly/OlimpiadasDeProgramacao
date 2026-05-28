#**Questão 3 — Simulador de um Pagamento**

#O programa deve ser executado em um laço de repetição `while`.

#João deseja efetuar um pagamento de uma conta, com as seguintes opções:
#- 1: À vista dinheiro com 10% de desconto.
#- 2: À vista no cartão com 5% de desconto.
#- 3: Até 2 parcelas no cartão sem desconto.
#- 4: 3 parcelas ou mais com 20% de juros do total da compra.

#**Regra:** O usuário deve escolher uma dessas opções, e deve aparecer o valor final a ser calculado, dependendo da situação. Se o usuário digitar o número 0 nas opções, encerre o programa.

#O programa deve pedir o preço da compra.

print("---- NOTA FISCAL ----")

valor_da_compra = float(input("Digite o valor das compras: R$ "))
    
while True: 
    print("""
        ESCOLHA UMA OPÇÃO DE PAGAMENTO:
        
        01 - À VISTA DINHEIRO
        02 - À VISTA NO CARTÃO 
        03 - PARCELADO NO CARTÃO ATE 2X
        04 - PARCELADO NO CARTÃO 3X OU MAIS
        0  - SAIR 
        """)

    opcao = input("DÍGITE A OPÇÃO DESEJADA:")
    total = 0
    
    if opcao == 1 :
        total = valor_da_compra - (valor_da_compra * 0.1)
        desconto = valor_da_compra * 0.1
        print(f"Sua compra {valor_da_compra:.2f}, custará R$ {total:.2f}, seu desconto será de R$ {desconto}.")
    
    elif opcao == 2 :
        total = valor_da_compra - (valor_da_compra * 0.05)
        desconto = valor_da_compra * 0.05
        print(f"Sua compra {valor_da_compra:.2f}, custará R$ {total:.2f}, seu desconto será de R$ {desconto}.")
    
    elif opcao == 3 :
        total = valor_da_compra 
        qtd_parcelas = total / 2
        desconto = 0
        print(f"Compra parcelada N° de parcelas 2 de R$ {qtd_parcelas}, sem juros. ")
    
    elif opcao == 4:
        total = valor_da_compra + (valor_da_compra * 0.2)
        qtd_parcelas = int(input("Escolha a quantidade de parcelas:"))
        parcela = total / qtd_parcelas
        desconto = 0
        print(f"Compra parcelada em {qtd_parcelas} de R$ {parcela:.2f} com juros de 20% ")
        
        print(f"Sua compra {valor_da_compra:.2f}, custará R$ {total:.2f}, seu desconto será de R$ {desconto}.") 
        
    elif opcao == 0:
        print("O PROGRAMA SERÁ ENCERRADO!")
        break
    

