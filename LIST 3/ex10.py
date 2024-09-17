num = int(input("Digite um número inteiro: "))
if num <= 0:
    print("!Digite um número inteiro positivo! ")
else:
    c = 0
    n = 1
    while c < num:
        if n % 2 != 0:
            print(n)
            c = c + 1
        n = n + 1
