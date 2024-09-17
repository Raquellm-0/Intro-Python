num = int(input("Digite um número: "))
maior = num
menor = num

while num > 0:
    if num > maior:
        maior = num 
    if num < menor:
        menor = num
    num = int(input("Digite um número: "))
print("Maior número: ",maior)
print("Menor número: ",menor)
