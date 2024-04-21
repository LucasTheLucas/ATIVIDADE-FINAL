Num = int(input("Digite um número: "))

ioo = Num // 100
oio = (Num % 100) // 10
ooi = Num % 10

print(f"A soma desses algarismos é de: {ioo + oio + ooi}")