# Equipe resolutora: Expressos Vermelhos de Monty
# Integrantes: Aline, Denzel, Lay e Stefano

# Questão 3 — Descontos e Gorjetas 
# Equipe autora: Nome não informado

# Um restaurante precisa calcular um desconto de 10% em cima do valor de um cliente caso seu consumo for acima de R$ 150. Caso não tiver desconto informe também. Logo após calcule a gorjeta do garçom: se o valor do cliente for maior que R$ 200, o garçom recebe 10% desse valor, se for acima de R$ 300, o garçom recebe 15% do valor. Imprima a nota fiscal no final. 


print(" ---- Restaurante Nome não informado ---- ")

valor = float(input("Digite o valor da conta do cliente: R$ "))

if valor <= 150:
    desconto = 0
    mens_desconto = "desconto não aprovado"
    valor_novo = valor
    gorjeta = 0
    mens_gorjeta = "Sem comissão"

elif valor > 150:
    desconto = 0.10
    mens_desconto = "desconto aprovado"
    valor_novo = valor - (valor * desconto)
    mens_gorjeta = "Sem comissão"
    gorjeta = 0

    if valor > 200 and valor <= 300:
        mens_gorjeta = "Ganhou comissão de 10%"
        gorjeta = valor * 0.10
            
    elif valor > 300:
        mens_gorjeta = "Ganhou comissão de 15%"
        gorjeta = valor * 0.15

print(f"""
        ------ Nota Fiscal ------ 
        
    Valor da Compra: R$ {valor:.2f}
    Desconto da Compra: {mens_desconto}!
        
     Valor Total: R$ {valor_novo:.2f}

        ------ Gorjeta do Garçom ------
        {mens_gorjeta}.
        R$ {gorjeta:.2f}
""")