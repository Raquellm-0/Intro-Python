try:
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite outro número: "))
    if num1 > num2:
        print(f"{num1} é maior!")
    if num1 < num2:
        print(f"{num2} é maior!")
    if num1 == num2:
        print("Números iguais!")
except:
    print("Digite um número!")
    