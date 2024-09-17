i = 0
n = int(input("Digite um número inteiro: ")) 
if n < 0:
    print("Digite um número inteiro positivo: ") 
else:
    while n > i:
        print(n)
        n = n - 1
print(n)
#decrescente