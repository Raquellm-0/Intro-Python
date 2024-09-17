n = int(input("Digite um número: "))
cont = 0 
while n >- 1:
    if (cont % 2 == 0):
        n -= 1
        cont += 1
    else:
        print(cont)
        cont += 1