num1 = int(input("Digite um número:"))
num2 = int(input("Digite um outro número:"))

if num1 > num2:
    print(f"{num1} é maior que {num2} a diferença entre ele é de: ",num1-num2)
elif num1 < num2:
    print(f"{num2} é maior que {num1} a diferença entre ele é de: ",num2-num1)
else:
    print("Números Iguais")