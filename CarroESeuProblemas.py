# Meu carro na gasolina fa 12KM/L e no etanol faz 8.5 KM/L.
# Qual compensa abastecer? Faça um algoritimo citando os dados
valGas = float(input("Quanto é o valor da gasolina?"))
KMGas = float(input("e quantos KM anda por litro com gasolina?"))
valEta = float(input("Quanto é o valor do etanol?"))
KMEta = float(input("e quantos KM anda por litro com Etanol?"))

gas = valGas/KMGas
eta = valEta/KMEta

if gas > eta:
    print(f"Etanol é mais custo beneficio!\nSeu carro anda {KMEta}KM/L\nE cada KM custa {eta}")
else:
    print(f"Gasolina é mais custo beneficio!\nSeu carro anda {KMGas}KM/L\nE cada KM custa {gas}")
