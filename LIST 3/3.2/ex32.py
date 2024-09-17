i = 0
numeros = []
while i < 5:
    num = int(input("Digite um número: "))
    numeros.append(num)
    i += 1
print("Soma: ")
print(sum(numeros))
for num in numeros:
    print(num)
