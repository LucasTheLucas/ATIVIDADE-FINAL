numero = int(input("DIGITE UM NÚMERO: "))
por5 = False
por3 = False

if(numero % 3 == 0):
    por3 = True

if(numero % 5 == 0):
    por5 = True

if(por5 and por3):
    print("Pode ser divido por 5 e 3")

elif (por5 == False and por3 == True):
    print("Pode ser dividido por 3")

elif (por5 == True and por3 == False):
    print("Pode ser dividido por 5")

else:
    print("Não pode ser dividido por 5 e 3")