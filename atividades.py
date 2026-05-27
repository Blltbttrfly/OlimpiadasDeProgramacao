#**Questão 2 — Simulador de Alistamento Militar**

#Joao deseja se alistar no serviço militar porém é preciso analisar sua idade.

#**Regra:** O programa deve informar se já é hora de alistar ou já passou o tempo do alistamento. Deve conter o tempo que falta para se alistar ou o prazo que passou. (No Brasil, o alistamento é obrigatorio aos 18 anos de idade.)

#O programa deve pedir:
#1. O ano de nascimento do solicitante.
print("---- SEJA BEM VINDO AO SERVICO DE ALISTAMENTO----")

nome_canditato = input("Digite o seu nome:")

ano_de_nascimento = int(input("Digite o ano de nascimento:"))

ano_atual = 2026

idade = ano_de_nascimento - ano_atual

while True:
    idade == 18 
    print(f"Cadastro Realizado com sucesso")
    break
    
if idade < 18 :
    print(f"Você não está apto para se alistar!")
    
elif idade > 18 :
    print(f"Seu tempo de alistamento expirou!")
    
 