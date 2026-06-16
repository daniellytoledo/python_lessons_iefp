from itertools import count

print("\n")
print(":"*50)
titulo = "TUPLAS"
print(f"{titulo:-^50}")
print(":"*50)
print("\n")

semana = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo")

# print no terceiro dia da semana

print(f"O terceiro dia da semana é {semana[2]}")

print("\n")
print(":"*49)
print("\n")

# tentar mudar um dos elementos da tupla :: não é possível alterar os elementos de uma tupla

try:
    semana[2] = "Quarta-feira"
except TypeError as e:
    print(f"Erro: {e}")

print("\n")
print(":" * 49)
print("\n")

# converter tupla para uma lista e adiciona um elemento e depois converte de volta para tupla

nomes = ("dani", "géssica", "joão", "eduardo", "andressa")
nomes_lista = list(nomes)
nomes_lista.append("vitor")
nomes_tupla = tuple(nomes_lista)
print(nomes_tupla)

print("\n")
print(":"*49)
print("\n")

# criar uma tupla com coordenadas (x, y) e desempacotar os valores em variáveis separadas

coordenadas = (10, 5)
x, y = coordenadas
print(f"A primeira coordenada é {x} e a segunda é {y}")

print("\n")
print(":"*49)
print("\n")

# criar uma tupla com os meses do ano e conta quantas vezes o mês de janeiro aparece

meses = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro", "Janeiro")

qnt_janeiro = meses.count("Janeiro")
print(f"Janeiro aparece apenas {qnt_janeiro} vez(es).")
print("\n")

# mostrar o índice de algum mês

print("Março tem índice: ", meses.index("Março"))
print("\n")

# saber quantos meses termina em "eiro"
qnt_eiro = []
qnt_embro = []
qnt_outros = []

for m in meses:
    if m.endswith("eiro"):
        qnt_eiro.append(m)
    elif m.endswith("embro"):
        qnt_embro.append(m)
    else:
        qnt_outros.append(m)

print(f"Existem {len(qnt_embro)} meses acabados com 'embro'.")
print(f"Existem {len(qnt_eiro)} meses acabados com 'eiro'.")
print(f"Existem {len(qnt_outros)} meses acabados com outras letras.")

print("\n")
print(":"*49)
print("\n")

# saber o index de um número de uma tupla

n = (1, 2, 3, 4, 5)
print(f"O índice do número 3 é: ", n.index(3))

