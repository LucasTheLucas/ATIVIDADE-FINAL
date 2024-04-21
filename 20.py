idade = int(input("Digite a idade: "))
trabalho = int(input("Digite o tempo de trabalho: "))

if(idade >= 65 or trabalho >= 30 or (trabalho>=25 and idade >=60)):
    print("Pode se aposentar")

else:
    print("Não pode se aposentar")