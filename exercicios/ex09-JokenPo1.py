import random

print("-"*49)
print("-"*20, "\033[1;7mJOKENPÔ\033[m", "-"*20)
print("-"*49)
print("\n")

opcoes     = ["pedra", "papel", "tesoura"]
computador = []

while True:
    computador = random.choice(opcoes)
    print("O COMPUTADOR ESCOLHEU! Agora é a sua vez.")

    print("\n")

    r = input("Escolha pedra, papel ou tesoura: ").lower()
    if r == computador:
        print("Empate!")
    elif r == "pedra" and computador == "tesoura":
        print("Ganhaste! O computador escolheu tesoura.")
    elif r == "papel" and computador == "pedra":
        print("Ganhaste! O computador escolheu pedra.")
    elif r == "tesoura" and computador == "papel":
        print("Ganhaste! O computador escolheu papel.")
    elif r == "tesoura" and computador == "pedra":
        print("Perdeste! O computador escolheu pedra.")
    elif r == "pedra" and computador == "papel":
        print("Perdeste! O computador escolheu papel.")
    elif r == "papel" and computador == "tesoura":
        print("Perdeste! O computador escolheu tesoura.")
    else:
        print("Opção incorreta! Digite novamente.")

    print("\n")

    encerrar = input("Desejas tentar de novo? [S/N] ").lower()
    if encerrar == "n":
        break
    elif encerrar == "s":
        r = input("Escolha pedra, papel ou tesoura: ").lower()
    else:
        print("Caractere não reconhecido. Tente novamente.")
