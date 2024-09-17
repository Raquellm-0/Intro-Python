num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

soma = 0
mult = 1
while num1 <= num2:
    if num1 % 2 == 0:
        soma = soma + num1
    else:
        mult *= num1
    num1 = num1 + 1
print("Soma dos números pares: ",soma)
print("Soma dos números ímpares: ",mult)
