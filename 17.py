ope = int(input("Escolha entre essas operaçoes matematícas:\n1.+\n2.-\n3.*\n4./\nNúmero da operação: "))
val1 = float(input("Digite um número: "))
val2 = float(input("Digite um número: "))

match ope:
    case 1:
        print(val1+val2)
    case 2:
        print(val1-val2)
    case 3:
        print(val1*val2)
    case 4:
        print(val1/val2)