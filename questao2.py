# Questão 2 — Banho de animais

# Fernando precisava de um sistema que organizasse os preços de banho dos animais.

# Crie um programa que receba o nome do animal e informe o valor do serviço, declare uma lista com alguns animais.

# Exemplo de execução:

# Valores do banho dos animais
# Digite o nome do animal: Gato
# Gato | R$ 35.0

animais_precos = {
    "cachorro": 2500,
    "gato": 1800,
    "papagaio": 1200,
    "coelho": 300,
    "hamster": 80,
    "peixe": 50,
    "cavalo": 1500,
    "tartaruga": 600
}
print("Bem vindo ao pet-shop eguinha pocotó")
print()
print("""
----PREÇOS----
cachorro: 2500,
gato: 1800,
papagaio: 1200,
coelho: 300,
hamster: 80,
peixe: 50,
cavalo: 1500,
tartaruga: 600
""")

while True:
    
    animal_escolhido = input("Digite o animal que deseja banhar: ").lower()
    if animal_escolhido in animais_precos:
        preco = animais_precos[animal_escolhido]
        print(f"{animal_escolhido} | R$ {preco:.2f}")
        break
    else:
        print("Não fazemos serviços para o animal listado.")
        continue




