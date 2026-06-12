print("\n")
print("::::::::::::::::::::::::::::::::::::::::::::::::::")
print("                    SOMA DE NÚMEROS - FOR ")
print("::::::::::::::::::::::::::::::::::::::::::::::::::")
print("\n")

lista = []

for i in range (5):
    n = int(input("Digite um número: "))
    lista.append(n)

print("\n")
print("Os números escolhidos foram: ", lista)
print("\n")

print("A soma dos números dentro desta lista é: ", sum(lista))

print("\n")
print("::::::::::::::::::::::::::::::::::::::::::::::::::")
print("                    SOMA DE NÚMEROS - WHILE ")
print("::::::::::::::::::::::::::::::::::::::::::::::::::")
print("\n")

nomes = []

while True:
    nome = input("Digite um nome: ")
    nomes.append(nome)
    r = input("Desejas continuar? [S/N] ").upper()
    if r == "N":
        break

print(nomes)
