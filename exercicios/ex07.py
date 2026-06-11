import time

print("\n")
print("::::::::::::::::::::::::::::::::::::::::::::::::::")
print("                    WHILE")
print("::::::::::::::::::::::::::::::::::::::::::::::::::")
print("\n")

# Ciclos permitem repetir ações sobre uma sequência (lista, range, string, etc.) ou um número de vezes. For é o ciclo mais usado para percorrer sequências. Embora o while seja mais flexível, o for é mais simples e legível para a maioria dos casos de iteração.

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
contador = 0
while contador < 5:
    print("Contador =", contador)
    time.sleep(0.5)
    contador += 1  # incrementa para não ficar em loop infinito

print("\n")

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
string = "Zarabatana"
contador = 0
limite = 5
while contador < limite:
    print(string[contador])
    contador += 1
    time.sleep(0.5)

