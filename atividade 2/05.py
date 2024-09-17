i = 0
fim = False
while fim == False:
    num = int(input("Digite um número ou -999 para finalizar: "))
    if num == -999:
         fim = True
    else:
        if num % 2 != 0:
         i = i + 1
print("Total de números ímpares: ",i)
