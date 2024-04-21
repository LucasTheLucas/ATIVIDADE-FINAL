n1 = float(input("Digite a primeira nota do aluno: "))
n2 = float(input("Digite a segunda nota do aluno: "))

if n1 >= 0 and n1 <= 10 and n2 >= 0 and n2 <= 10:
    print(f"A média é de: {(n1+n2)/2}")

else:
    print("Uma da notas se não as duas são invalidas!")