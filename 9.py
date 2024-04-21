Salario = float(input("Digite o sálario do trabalhador: "))
ValorEmprestimo = float(input("Digite o valor do emprestimo: "))

Salario20Porcento = Salario * 0.2

if(ValorEmprestimo <= Salario20Porcento):
    print("O emprestimo pode ser feito!")

else:
    print("O emprestimo não pode ser feito!")