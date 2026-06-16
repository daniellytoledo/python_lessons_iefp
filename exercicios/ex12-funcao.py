print("\n")
print(":"*49)
titulo = "FUNÇÕES"
print(f"{titulo:-^49}")
print(":"*49)
print("\n")


def saudacao2(nome):
    print("Olá,", nome,"!")
    print(f"Olá, {nome}!")

saudacao2("João")

print("\n")
print(":"*49)
print("\n")

def saudacao1(nome):
    return f"Olá, {nome}!"

print(saudacao1("DANI"))

print("\n")
print(":"*49)
print("\n")

def pessoas(nome1, nome2):
    return f"{nome1} e {nome2} estão namorando."

print (pessoas("dani", "who"))

print("\n")
print(":"*49)
print("\n")

def soma(a, b):
    return a, b, a + b

a, b, resultado = soma(2, 3)
print(f"A soma de {a} e {b} é {resultado}!")

print("\n")
print(":"*49)
print("\n")

valor1 = 10
valor2 = 3
divisao = 10/3

# :.2f formatando o resultado em 2 decimais
print(f"A divisão de {valor1} por {valor2} é {divisao:.2f}!")

# :^15.2f está formatando divisão, colocando-o entre 15 espaços vazios com 2 casas decimais
print(f"A divisão de {valor1} por {valor2} é {divisao:^15.2f}!")

# :*>15.2f colocando * no lado esquerdo enquanto usa 15 "espaços" no total
print(f"A divisão de {valor1} por {valor2} é {divisao:*>15.2f}!")

# :*<15.2f colocando * no lado direito enquanto usa 15 "espaços" no total
print(f"A divisão de {valor1} por {valor2} é {divisao:*<15.2f}!")

# :-^15 coloca o resultado de divisão no meio de - usando 20 caracteres no total
print(f"A divisão de {valor1} por {valor2} é {divisao:-^20.2f}!")



