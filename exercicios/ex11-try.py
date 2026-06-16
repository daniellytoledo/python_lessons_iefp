# número dentro de intervalo
# pede uma nota entre 0 e 20
# se for inválido ou fora do intervalo, volta a pedir

print("\n")
print(":"*49)
print("  SOLICITAR UMA NOTA NO INTERVALO DE 0 A 20 ")
print(":"*49)
print("\n")

while True:
    try:
        nota = float(input("Digite um valor entre 0 a 20: ").replace(",", "."))
        if 0 <= nota <= 20:
            print("Nota recebida com sucesso!")
            break
        else:
            print("A nota tem que estar entre 0 e 20")
    except ValueError:
        print("ERRO: Digite um número válido.")