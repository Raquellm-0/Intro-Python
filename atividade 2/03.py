valor = int(input("Digite o valor do seu saque (10-600): "))
if valor < 10 or valor > 600:
    print("!!Impossivel realizar saque!!!\n Valor mínimo:  R$10\n Valor máximo: R$600")
else:
    n100 = valor // 100
    valor %= 100
    n50 = valor // 50
    valor %= 50
    n10 = valor // 10
    valor %= 10
    n5 = valor // 5
    valor %= 5
    n1 = valor
    print("Você irá receber: ")
    print(n100, "notas de R$100")
    print(n50, "notas de R$50")
    print(n10, "notas de R$10")
    print(n5, "notas de R$5")
    print(n1, "notas de R$1")