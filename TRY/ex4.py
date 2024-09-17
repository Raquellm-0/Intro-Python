try:
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        print("É par!")
    if num % 2 != 0:
        print("É ímpar!")
except:
    print("Digite um valor válido!")