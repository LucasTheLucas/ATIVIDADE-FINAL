Idade = int(input("Digite a idade do jogador de bocha: "))
classe = ""

if Idade < 5:
    print("JOGADOR INADEQUADO PARA JOGAR")

elif Idade >= 5 and Idade <= 7:
    classe = "Infantil A"

elif Idade >= 8 and Idade <= 10:
    classe = "Infantil B"

elif Idade >= 11 and Idade <= 13:
    classe = "Juvenil A"

elif Idade >= 14 and Idade <= 17:
    classe = "Juvenil B"

else:
    classe = "Senior"

print(f"A classe de um jogador com {Idade} anos é de {classe}")

