ValorDaVenda = float(input("Digite o valor do produto: "))
estado = int(input("Selecione um estado:\n1.MG\n2.SP\n3.RJ\n4.MS\nOpção: "))
taxa = 0

match estado:
    case 1:
        taxa = 0.07
    case 2:
        taxa = 0.12
    case 3:
        taxa = 0.15
    case 4:
        taxa = 0.08
    case _:
        print("Número de opção invalido tente novamente")

print(f"Valor total a ser pago é de {ValorDaVenda + (ValorDaVenda * taxa)}R$")
