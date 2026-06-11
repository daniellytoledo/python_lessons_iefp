print("\n")
print("::::::::::::::::::::::::::::::::::::::::::::::::::")
print("RECEBER DADOS DO UTILIZADOR")
print("::::::::::::::::::::::::::::::::::::::::::::::::::")
print("\n")

idade        = int(input("Qual a sua idade? "))
altura_string = input("Qual a sua altura em metros? ")
altura       = float(altura_string.replace(",", "."))

print("\n")

# operadores simples

anos_mais   = idade + 5
altura_mais = altura + 0.1

print("Daqui a 5 anos terás", anos_mais, "anos.")
print(("Se cresceres 10cm, terás", altura_mais, "metros."))

print("\n")