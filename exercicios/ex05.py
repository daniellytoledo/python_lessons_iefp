print("\n")
print("::::::::::::::::::::::::::::::::::::::::::::::::::")
print("            IF E OPERADORES LÓGICOS")
print("::::::::::::::::::::::::::::::::::::::::::::::::::")
print("\n")

# exercício: aptidão para ser astronauta?
# é necessário boa vista
# altura superior a 1.8m
# idade entre 20 e 40 anos

visao  = input("Tens boa visão? [S/N] ").lower() == "s"
altura = float(input("Qual a sua altura? ").replace(",", ".")) >= 1.8
idade = int(input("Qual a sua idade? "))
idade_necessaria = 20 <= idade <= 40

print("\n")
print(":::::::::::: RESULTADO ::::::::::::")

if visao and altura and idade_necessaria:
    print("Estás apto para ser um astronauta?")

else:
    print("Não estás apto para ser um astronauta.")

print("\n")
print(":::::::::::: RESULTADO ::::::::::::")

