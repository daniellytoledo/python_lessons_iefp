from traceback import print_tb

print("\n")
print("::::::::::::::::::::::::::::::::::::::::::::::::::")
print("                    CALCULAR IMC")
print("::::::::::::::::::::::::::::::::::::::::::::::::::")
print("\n")

# Classificação completa das faixas:

# Magreza grave: IMC < 16
# Abaixo do peso: IMC entre 16 e 18,5
# Peso adequado: IMC entre 18,5 e 25
# Acima do peso: IMC entre 25 e 29,9
# Obesidade Grau I: IMC entre 30 e 34,9
# Obesidade Grau II: IMC entre 35 e 39
# Obesidade Grau III ou mórbida: acima de 40


peso_string    = input("Digite seu peso: ")
peso           = float(peso_string.replace(",", "."))
altura_string  = input("Digite sua altura: ")
altura         = float(altura_string.replace(",", "."))
IMC            = peso / (altura ** 2)

print("\n")
print(":::::::::::: RESULTADO ::::::::::::")

if IMC < 16:
    print(":::::::::::: Atenção! Magreza grave! 😰")
elif IMC >= 16 and IMC < 18.5:
    print(":::::::::::: Abaixo do peso! 😢")
elif IMC >= 18.5 and IMC < 25:
    print(":::::::::::: Peso ideal! 👌")
elif IMC >= 25 and IMC < 29.9:
    print(":::::::::::: Obesidade Grau I! 😮")
elif IMC >= 30 and 34.9:
    print(":::::::::::: Obesidade Grau II! ☠️")
elif IMC >= 40:
    print(":::::::::::: Obesidade Grau III! 👻")

# CÓDIGO OTIMIZADO

print("\n")
print(":::::::::::: CÓDIGO OTIMIZADO ::::::::::::")

if IMC < 16:
    print(":::::::::::: Atenção! Magreza grave! 😰")
elif IMC <= 18.5:
    print(":::::::::::: Abaixo do peso! 😢")
elif IMC <= 25:
    print(":::::::::::: Peso ideal! 👌")
elif IMC <= 29.9:
    print(":::::::::::: Obesidade Grau I! 😮")
elif IMC <= 40:
    print(":::::::::::: Obesidade Grau II! ☠️")
elif IMC >= 40:
    print(":::::::::::: Obesidade Grau III! 👻")


