# Equipe resolutora: Expressos Vermelhos de Monty
# Integrantes: Aline, Denzel, Lay e Stefano

# Questão 2 — Simulador de Alistamento Militar
# Equipe autora: VibeCodianos

# João deseja se alistar no serviço militar porém é preciso analisar sua idade.

# Regra: O programa deve informar se já é hora de alistar ou já passou o tempo do alistamento. Deve conter o tempo que falta para se alistar ou o prazo que passou. (No Brasil, o alistamento é obrigatorio aos 18 anos de idade).

# O programa deve pedir: O ano de nascimento do solicitante.


nome = input("Digite o seu nome: ")
ano_nasc = int(input("Digite o seu ano de nascimento: "))

verificar_idade = 2026 - ano_nasc

if verificar_idade >= 18:
    print(f"Olá, {nome}! O seu prazo de alistamento militar passou! Você já tem {verificar_idade} anos.")
elif verificar_idade < 18:
    print(f"Olá, {nome}! Fantam {verificar_idade} anos para o seu período de alistamento!")
else:
    print("Erro em alguma informação fornecida. Tente novamente!")