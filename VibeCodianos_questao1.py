# Equipe resolutora: Expressos Vermelhos de Monty
# Integrantes: Aline, Denzel, Lay e Stefano

# Questão 1 — Simulador de Emprestimo bancario
# Equipe autora: VibeCodianos

# Maria deseja solicitar um empréstimo bancário ao banco para o financiamento de uma casa. O banco possui regras claras para aprovar ou negar o crédito bancário.

# Regra: O empréstimo será aprovado quando a prestação mensal não exceder 30% de seu salário.

# O programa deve receber:
# O valor da casa que será financiada pelo banco.
# O valor do salário da pessoa que deseja o financiamento.
# Quantos anos de financiamento do empréstimo.
# Calcule se o valor do empréstimo for maior ou menor que o salário de Maria. Se o valor da prestação exceder o limite de 30% do salário, empréstimo negado. Se o valor da prestação não exceder o limite, empréstimo aprovado.


nome = input("Digite o seu nome: ")
salario = float(input("Digite o seu salário: "))
valor_casa = float(input("Digite o valor da casa que deseja financiar: "))
anos_finan = int(input("Em quantos anos deseja financiar a casa? "))

valor_prestacao = valor_casa/anos_finan
limite = salario * 0.3

if valor_prestacao <= limite:
    print("Empréstimo aprovado!")
elif valor_prestacao > limite:
    print("Empréstimo negado!")