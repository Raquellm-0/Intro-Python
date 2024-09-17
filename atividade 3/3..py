par = impar = 0
vetor = 0
for vetor in range(20):
    num = int(input("Digite um número inteiro: "))
    if num % 2 == 0:
     par = par + 1
    elif num % 2 != 0:
        impar = impar + 1
print("Total de números pares:",par)
print("Total de números ímpares:",impar)
