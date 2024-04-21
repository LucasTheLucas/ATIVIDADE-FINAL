Prova1 = float(input("Digite o valor da prova 1: "))
Prova2 = float(input("Digite o valor da prova 2: "))

Media = (Prova1 + (Prova2 * 2))/3

if(Media >= 7):
    print(f"Sua média foi de {Media} [APROVADO]")

else:
    print(f"Sua média foi de {Media} [REPROVADO]")