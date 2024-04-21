Ano = int(input("Digite o ano que você quer descobrir se é bissexto"))

if Ano % 400 == 0:
    print("Esse ano é bissexto")
        
elif Ano % 4 == 0 and Ano % 100 != 0:
    print("Esse ano é bissexto")

else:
    print("Esse ano não é bissexto")