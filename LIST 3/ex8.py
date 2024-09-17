i = 0
soma = 0
while i < 10:
    num = int(input("Digite um número inteiro: "))
    if num > 0:
        soma = soma + num
        i = i + 1
    else:
        continue
media = soma / i
print("Média de: ",media)
