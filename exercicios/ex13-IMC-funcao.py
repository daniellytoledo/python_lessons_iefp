print("\n")
print(":"*50)
titulo = "CALCULAR IMC COM FUNÇÃO"
print(f"{titulo:-^50}")
print(":"*50)
print("\n")

def calcular_imc():
    altura = float(input("Digite sua altura: ").replace(",", "."))
    peso = float(input("Digite seu peso: ").replace(",", "."))
    return altura, peso, peso / (altura ** 2)

altura, peso, imc = calcular_imc()
print(f"Sua altura é {altura}m, peso é {peso}kg e seu IMC é {imc:.2f}.")

def classif_imc():
    if imc < 16:
        print(":::::::::::: Atenção! Magreza grave! 😰")
    elif imc <= 18.5:
        print(":::::::::::: Abaixo do peso! 😢")
    elif imc <= 25:
        print(":::::::::::: Peso ideal! 👌")
    elif imc <= 29.9:
        print(":::::::::::: Obesidade Grau I! 😮")
    elif imc <= 40:
        print(":::::::::::: Obesidade Grau II! ☠️")
    elif imc >= 40:
        print(":::::::::::: Obesidade Grau III! 👻")

print(classif_imc(imc))
