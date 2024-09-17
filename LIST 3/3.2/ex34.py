numeros = []
p = []
i = []
v = 0
while v < 5:
    num = int(input("Digite um número: "))
    numeros.append(num)
    if num % 2 == 0:
        p.append(num)
    else:
        i.append(num)
    v = v + 1
print("Números digitedos: ",numeros)
print("Total de números: ",sum(numeros))
print("Números pares: ",p)
print("Números impares: ",i)
