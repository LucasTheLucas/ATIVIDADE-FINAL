a = float(input("Digite o tamanho do lado A: "))
b = float(input("Digite o tamanho do lado B: "))
c = float(input("Digite o tamanho do lado C: "))

Ab = a+b
Bc = b+c
Ca = c+a

if(Ab > c and Bc > a and Ca > b):
    if(a == b == c):
        print("Triangulo equilatero")

    elif(a != b != c):
        print("Triangulo escaleno")

    else:
        print("Triangulo isoselis")

else:
    print("Um triangulo com lados desse tamanho não exite")