MesDOANO = int(input("Digite um número entre 1 e 12: "))
text = ""
match MesDOANO:
    case 1: text = "Janeiro"
    case 2: text = "Fevereiro"
    case 3: text = "Março"
    case 4: text = "Abril"
    case 5: text = "Maio"
    case 6: text = "Junho"
    case 7: text = "Julho"
    case 8: text = "Agosto"
    case 9: text = "Setembro"
    case 10: text = "Outubro"
    case 11: text = "Novembro"
    case 12: text = "Dezembro"

print(text)