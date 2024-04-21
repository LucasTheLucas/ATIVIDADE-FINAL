import math
horaChegada = int(input("Digite a hora que você chegou: "))
minutoChegada = int(input("Digite os minutos que você chegou: "))
horaSaida = int(input("Digite a hora que você saiu: "))
minutoSaida = int(input("Digite os minutos que você saiu: "))
tempoDecorido = 0
if horaChegada > horaSaida:
    tempoDecorido = horaSaida + (24 - horaChegada)
    tempoDecorido = (tempoDecorido * 60)
    if minutoChegada < minutoSaida:
        tempoDecorido = tempoDecorido + (minutoSaida - minutoChegada)
    
    else:
        tempoDecorido = tempoDecorido + (minutoChegada - minutoSaida)

else:
    tempoDecorido = horaSaida - horaChegada
    tempoDecorido = (tempoDecorido * 60)
    if minutoChegada < minutoSaida:
        tempoDecorido = tempoDecorido + (minutoSaida - minutoChegada)
    
    else:
        tempoDecorido = tempoDecorido + (minutoChegada - minutoSaida)

horasApagar = math.ceil(tempoDecorido/60)
taxa = 0

if horasApagar <= 0:
    print("Não precisa pagar")

elif horasApagar > 0 and horasApagar <= 2:
    taxa = 1

elif horasApagar > 2 and horasApagar <= 4:
    taxa = 1.40

else:
    taxa = 2

print(f"Você terá que pagar {horasApagar*taxa}R$")
