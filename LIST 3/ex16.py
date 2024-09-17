i = 1
n = int(input("Digite um número inteiro positivo ímpar: ")) 
if n % 2 == 0:
    print("!Digite um número ímpar! ") 
else:
    while n > i:
     if n % 2 != 0:
      print(i)
      i = i + 2
print(n)
#crescente
