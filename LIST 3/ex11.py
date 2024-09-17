soma = 0
cont = 0
num = 0
while cont < 50:
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
    num = num + 1
print("A soma dos primeiros 50 números:", soma)
