# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# TIPOS DE DADOS
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

idade = 30
altura = 1.75
nome = "João"
maior_de_idade = True
separador = ":::::::::::::::::::::::::::::::::::::::::::::::::::"

print(nome, "tem", idade,"anos e altura de", altura, "metros.")
print("Maior de idade:", maior_de_idade)
print("batatas")
print(separador)



# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# NÚMEROS
# Python tem dois tipos principais:
# int → números inteiros
# float → números com casas decimais 
idade = 30        # int
altura = 1.75     # float



# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# OPERADORES NUMÉRICOS
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.3333333333333335  -> sempre float
print(a // b)  # 3  -> divisão inteira
print(a % b)   # 1  -> resto da divisão
print(a ** b)  # 1000 -> potência

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# # OPERADORES DE COMPARAÇÃO

# &	interseção
# |	união
# ^	diferença simétrica
# ==	igual a
# !=   diferente de
# >	maior que
# <	menor que
# >=	maior ou igual a
# <=	menor ou igual a
# in    verificar se um elemento pertence a uma coleção

# Operadores lógicos
# and	verdadeiro se ambos os operandos forem verdadeiros
# or	verdadeiro se pelo menos um dos operandos for verdadeiro
# not	verdadeiro se o operando for falso

# Operadores de atribuição
# =	atribuição simples
# &=  atribuição com interseção
# |=  atribuição com união
# ^=  atribuição com diferença simétrica
# +=	adição e atribuição
# -=  subtração e atribuição
# *=	multiplicação e atribuição 
# /=  divisão e atribuição
# //= divisão inteira e atribuição
# **= potência e atribuição

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# STRINGS

# Sequência de caracteres
# Uma só linha: delimitados por  " ou ' 
# Multilinha: delimiotados por """ ou '''

nome = "João" 
# igual a 
nome = 'João'
sql = """
SELECT * FROM alugueres
LEFT JOIN clientes on alugueres.clientes
WHERE id=5
"""

# fstrings - permitem meter expressões dentro de {}
soma = f"2 + 2 = {2+2}"
output = f"O cliente {nome} foi adicionado com sucesso"
caminho = f"/cliente/{id}"  # muito usada no flask

#raw strings - desliga os escapes
path = r"venv\Scripts\activate"

print(nome[0])   # 'J'  -> acesso a carácter
print(nome[-1])  # 'o'  -> último carácter
print(nome[1:3]) # 'oã' -> slice

lista = [0,2,4,6]
dicionario = {
    "nome"      : "Pedro",
    "morada"    : "Tavira"
}

print(separador)
if "nome" in dicionario:
    if(dicionario['nome'] == "Pedro"):
        print("Pedro consta sim sr")
else:
    print("Não consta")
print(separador)

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# funções úteis:
nome.upper()   # 'JOÃO'
nome.lower()   # 'joão'
nome.replace("ã", "a")  # 'Joao'
len(nome)      # 4
nomes = ["João","Vicente","Valente","Lapa"]
nc = " ".join(nomes)
print(nc)
print(f"A lista dos nomes tem {len(nomes)} elementos")
print("A lista dos nomes tem {len(nomes)} elementos")



# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# BOOLEANOS

# True ou False
# Usados para condições

maior = idade >= 18
print(maior)   # True

apto = altura >= 1.75 and maior
print(apto)    # True


# Regra geral
# Python considera como False quando o container está vazio.
# Qualquer um dos seguintes é falso em contexto booleano: 
0
""
[]
{}
set()
None
resultado = [1]

print("Avaliação de Booleanos :::::::::::::::::::::::::")
if resultado:
    print("resultado é verdadeiro")
else:
    print("resultado é falso")
print("Fim da avaliação de Booleanos :::::::::::::::::::::::::")

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# Tuplas

# Coleção ordenada, imutável
# Sintaxe: (elem1, elem2, ...)
# Útil para devolver múltiplos valores de uma função:

coordenadas = (10.0, 20.0)
# coordenadas[0] = 5  -> erro!
print(coordenadas[1])  # 20.0

def exemplo():
    # algoritmia
    return 1, 2  # devolve um tuplo

x, y = exemplo()
print(x)  # 1
print(y)  # 2


# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# Listas

# Coleção ordenada e mutável
# Sintaxe: [elemento1, elemento2, ...] 

frutas = ["maçã", "banana", "laranja"]
frutas.append("kiwi")   # adiciona
frutas.pop(1)           # remove índice 1
print(frutas[0])        # 'maçã'
print(frutas)


# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# Dicionários

# Coleção de pares chave: valor
# Sintaxe: {"chave": valor} 

pessoa = {
    "nome": "Ana", 
    "idade": 25
}
print(pessoa["nome"])   # Ana
pessoa["altura"] = 1.65 # adiciona novo par
print(pessoa)


# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# Set

# Coleção não ordenada, sem duplicados
# Sintaxe: {elem1, elem2} 

numeros = {1, 2, 3, 3}
print(numeros)   # {1, 2, 3}

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# None

# Representa ausência de valor
# Útil para inicializar variáveis 

idade2=50
adulto = None
crianca = None

if idade2 > 30:
    adulto = True
else:
    crianca = True

print(f"Criança: {crianca}")
print(f"Adulto: {adulto}")

resultado = None
if resultado is None:
    print("O valor ainda não foi calculado")


print(f"Criança é None? : {crianca is None}")

# comparações com None
# is None
# is not None
# INCORRETO:  == None


# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# EXERCÍCIOS

# 1 - Cria uma lista de 3 frutas e imprime cada uma.
# 2 - Cria um dicionário com nome, idade e altura e imprime “nome tem idade anos e mede altura metros”.
# 3 - Cria uma função que devolve múltiplos valores (tuplo) e depois descompacta-os em variáveis.
# 4 - Cria uma variável booleana maior baseada numa idade, e imprime “Maior de idade” se True ou “Menor de idade” se False.
# 5 - Cria um conjunto de números com valores repetidos e imprime o conjunto (deve eliminar duplicados).

