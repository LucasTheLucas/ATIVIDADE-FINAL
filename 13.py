#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
Lab = float(input("Digite a nota do trabalho de laboratorio: "))
Apr = float(input("Digite a nota da apresentação: "))
Ava = float(input("Digite a nota da avaliação :"))

Media = ((Lab * 2) + (Apr * 5) + (Ava * 3)) / 10

if Media >= 0 and Media <= 2.9:
    print(f"[REPROVADO]:{Media}")

elif Media >= 3 and Media <= 4.9:
    print(f"[RECUPERAÇÃO]:{Media}")

else:
    print(f"[APROVADO]:{Media}")    