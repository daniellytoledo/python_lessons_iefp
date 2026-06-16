print("\n")
print(":"*49)
titulo = "SOMA DE NÚMEROS - FOR + WHILE + TRY"
print(f"{titulo:-^49}")
print(":"*49)
print("\n")

lista = []

for i in range (5):
    while True:
        try:
            n = int(input("Digite um número: "))
            lista.append(n)
            break
        except Exception:
            print("ERRO: Tens que inserir um número inteiro.")

print("\n")
print("Os números escolhidos foram: ", lista)
print("\n")

print("A soma dos números dentro desta lista é: ", sum(lista))