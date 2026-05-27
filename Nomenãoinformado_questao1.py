#Questão 1 — Estoque de uma Farmácia

#Lucas precisa organizar o estoque de sua nova farmácia e precisa de um programa que ajude ele com esse processo.

#Crie um programa de gerenciamento de estoque com as seguintes funções:

#Cadastrar novo medicamento.
#Vizualizar medicamentos em estoque.
#Sair do sistema.


medicamentos = [ 
    {"Nome": "Amoxicilina", "Preço": 45.90, "Quantidade em estoque": 120},
    {"Nome": "Ibuprofeno", "Preço": 18.50, "Quantidade em estoque": 85},
    {"Nome": "Paracetamol", "Preço": 12.30, "Quantidade em estoque": 200},
    {"Nome": "Dipirona Monoidratada", "Preço": 15.20, "Quantidade em estoque": 150},
    {"Nome": "Omeprazol", "Preço": 28.90, "Quantidade em estoque": 90},
    {"Nome": "Losartana Potássica", "Preço": 22.40, "Quantidade em estoque": 110},
    {"Nome": "Simvastatina", "Preço": 35.60, "Quantidade em estoque": 65},
    {"Nome": "Cloridrato de Metformina", "Preço": 19.80, "Quantidade em estoque": 140},
    {"Nome": "Cetoconazol Creme", "Preço": 24.15, "Quantidade em estoque": 40},
    {"Nome": "Azitromicina", "Preço": 33.00, "Quantidade em estoque": 75}
]
while True:
    
    print(f"""
    ======= ESTOQUE DA FARMÁCIA ========
        1. cadastra novo medicamento.
        2. Vizualizar medicamentos em estoque.
        
        0. Sair do sistema.
    ====================================
    """)
    op = input("Digite a opção que queira acessar: ")

    if op == "1":
        while True:
            print("== Cadastro de Medicamentos ==")
            nome_novo_medicamento = input("Digite o nome do novo medicamento: ")
            if len(nome_novo_medicamento) < 2:
                print("Digite um nome com mais de 2 digitos!!!")
            else:
                break
        while True:
            novo_medicamento_preco = float(input("Digite o preço do novo medicamento: "))
            if novo_medicamento_preco < 0:
                print("Digite um preço válído")
            else:
                break
        while True:
            novo_medicamento_estoque = int(input("Digite a quatidade de medicamentos: "))
            if novo_medicamento_estoque < 0:
                print("Número inválido")
            else:
                break

        cadastro_medicamento = {
        "Nome":nome_novo_medicamento,
        "Preço":novo_medicamento_preco,
        "Quantidade em estoque":novo_medicamento_estoque
        }

        medicamentos.append(cadastro_medicamento)

    if op == "2":
            for medicamento in medicamentos:
                print(medicamento)

    if op == "0":
        while True:
            print("OBRIGADO PELA SUA ATENÇÃO")
            break