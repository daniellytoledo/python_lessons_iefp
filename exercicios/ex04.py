print("\n")
print("::::::::::::::::::::::::::::::::::::::::::::::::::")
print("            IF E OPERADORES LÓGICOS")
print("::::::::::::::::::::::::::::::::::::::::::::::::::")
print("\n")

# ler idade e altura do utilizador
# se for maior 1,75m é alto

idade  = int(input("digite sua idade: "))
altura = float(input("digite sua altura: ").replace(",", "."))

print("\n")
print(":::::::::::: RESULTADO ::::::::::::")

if altura >= 1.75 and idade >= 18:
    print("Você é considerado alto e é maior de idade.")
elif altura >= 1.75 and idade < 18:
    print("Você é considerado alto e é menor de idade.")
elif altura < 1.75 and idade < 18:
    print("Você é considerado baixo e é menor de idade.")
elif altura < 1.75 and idade >= 18:
    print("Você é considerado baixo e é maior de idade.")

print("\n")
print("::::::::::::::::::::::::::::::::::::::::::::::::::")
print("                CÓDIGO OTIMIZADO")
print("::::::::::::::::::::::::::::::::::::::::::::::::::")
print("\n")

adulto  = int(input("digite sua idade: ")) >= 18
alto = float(input("digite sua altura: ").replace(",", ".")) >= 1.75

print("\n")
print(":::::::::::: RESULTADO ::::::::::::")

if not adulto and not alto:
    print("És menor de idade e baixo.")
elif not adulto and alto:
    print("És menor de idade e alto.")
elif adulto and not alto:
    print("És maior de idade e baixo.")
elif adulto and alto:
    print("És maior de idade e alto.")