# número dentro de intervalo
# pede uma nota entre 0 e 20
# se for inválido ou fora do intervalo, volta a pedir

print("\n")
print(":"*49)
print("  SOLICITAR UMA NOTA NO INTERVALO DE 0 A 20 ")
print(":"*49)
print("\n")

def lancarNota():
    while True:
        try:
            nota = float(input("Digite um valor entre 0 a 20: ").replace(",", "."))
            if 0 <= nota <= 20:
                break
            else:
                print("A nota tem que estar entre 0 e 20")
        except ValueError:
            print("ERRO: Digite um número válido.")

    while True:
        r = input("Deseja adicionar mais uma nota? [S/N]").upper()
        if r == "S":
         lancarNota()
        elif r == "N":
         break
        else:
            print("Responda apenas 'S' ou 'N'.")