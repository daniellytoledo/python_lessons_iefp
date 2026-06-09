separador = "-----------------------------------------------------"

print(separador)
print("EXERCÍCIOS 1")
print(separador)

print("\n")

print(separador)
print("LISTA")
print(separador)

print("\n")

frutas = ["Pera", "Cereja", "Morango"]
print(frutas[0])
print(frutas[1])
print(frutas[2])

print("\n")

print(separador)
print("DICIONÁRIO")
print(separador)

print("\n")

dadosPessoais = {
    "nome"   : "Maria",
    "idade"  : "91",
    "altura" : 1.23
}

print(f"A {dadosPessoais['nome']} tem {dadosPessoais['idade']} anos e mede {dadosPessoais['altura']}m.")

print("\n")

print(separador)
print("FUNÇÃO")
print(separador)

print("\n")

def dobroTriploQuadruplo(n):
    dobro       = n * 2
    triplo      = n * 3
    quadruplo   = n * 4

    return dobro, triplo, quadruplo

valorEscolhido = int(input("Insira um valor numérico: "))

d, t, q = dobroTriploQuadruplo(valorEscolhido)

print(f"Dobro: {d}, triplo: {t}, quadruplo: {q}.")

print("\n")

print(separador)
print("BOOLEANA")
print(separador)

print("\n")

idade = 70
maior = idade >= 18

if maior:
    print("Maior de idade.")
else:
    print("Menor de idade.")

print("\n")

print(separador)
print("CONJUNTO SEM DUPLICADOS COM SET{}")
print(separador)

print("\n")

semDuplicadas = {1, 2, 2, 3, 4, 4, 5}

print(semDuplicadas)