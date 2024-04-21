DiaSemana = int(input("Digite um número entre 1 e 7: "))
text = ""
match DiaSemana:
    case 1: text = "Domingo"
    case 2: text = "Segunda"
    case 3: text = "Terça"
    case 4: text = "Quarta"
    case 5: text = "Quinta"
    case 6: text = "Sexta"
    case 7: text = "Sábado"

print(text)