i = 0
n = int(input("Digite um número inteiro positivo par: ")) 
if n < 0:
    print("Digite um número inteiro positivo par: ") 
else:
    while n > i:
     print(n)
     n = n - 2
print(n)
#decrescente