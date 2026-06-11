import time

print("\n")
print("::::::::::::::::::::::::::::::::::::::::::::::::::")
print("                    CICLOS")
print("::::::::::::::::::::::::::::::::::::::::::::::::::")
print("\n")

print(":::::::::::: números de 1 a 10 ::::::::::::")

# RANGE
for i in range(1,6):
    print(i, "💣")
    time.sleep(0.5)
print("💥💥💥💥💥")
print("💥💥☠️💥💥")
print("💥💥💥💥💥")

print("\n")

frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print("Eu gosto de ", fruta)

print("\n")

for letra in "danielly":
    print(letra)

print("\n")
print(":::::::::::::::::: listas :::::::::::::::::")
print("\n")

reclusos = [
    {
        "nome": "João Silva",
        "pena": "5 anos e 6 meses",
        "crime": "Furto qualificado",
        "e_prisional": "Estabelecimento Prisional de Lisboa",
        "data_nascimento": "1985-03-12"
    },
    {
        "nome": "Carlos Mendes",
        "pena": "12 anos",
        "crime": "Homicídio",
        "e_prisional": "Estabelecimento Prisional de Coimbra",
        "data_nascimento": "1978-07-25"
    },
    {
        "nome": "Ricardo Alves",
        "pena": "3 anos e 2 meses",
        "crime": "Tráfico de droga",
        "e_prisional": "Estabelecimento Prisional do Porto",
        "data_nascimento": "1990-11-05"
    },
    {
        "nome": "Miguel Rocha",
        "pena": "8 anos",
        "crime": "Roubo agravado",
        "e_prisional": "Estabelecimento Prisional de Braga",
        "data_nascimento": "1982-01-19"
    },
    {
        "nome": "Pedro Costa",
        "pena": "2 anos e 8 meses",
        "crime": "Burla",
        "e_prisional": "Estabelecimento Prisional de Leiria",
        "data_nascimento": "1995-06-30"
    },
    {
        "nome": "André Ferreira",
        "pena": "15 anos",
        "crime": "Violação",
        "e_prisional": "Estabelecimento Prisional de Évora",
        "data_nascimento": "1975-09-14"
    },
    {
        "nome": "Tiago Sousa",
        "pena": "4 anos",
        "crime": "Ofensa à integridade física",
        "e_prisional": "Estabelecimento Prisional de Setúbal",
        "data_nascimento": "1988-12-22"
    },
    {
        "nome": "Bruno Lopes",
        "pena": "6 anos e 3 meses",
        "crime": "Sequestro",
        "e_prisional": "Estabelecimento Prisional de Faro",
        "data_nascimento": "1983-04-10"
    },
    {
        "nome": "Nuno Martins",
        "pena": "10 anos",
        "crime": "Assalto à mão armada",
        "e_prisional": "Estabelecimento Prisional de Aveiro",
        "data_nascimento": "1979-08-03"
    },
    {
        "nome": "Fábio Gomes",
        "pena": "1 ano e 6 meses",
        "crime": "Condução sem carta",
        "e_prisional": "Estabelecimento Prisional de Viseu",
        "data_nascimento": "2000-02-17"
    },
]

for recluso in reclusos:
    print(f"{recluso['nome']} - {recluso['e_prisional']}")

    print(recluso['nome'], " - ", recluso['e_prisional'])