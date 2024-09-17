def maior(n1,n2,n3):
    if n1 > n2 and n1 > n3:
        return (f"O número {n1} é o maior!")
    if n2 > n1 and n2 > n3:
        return (f"O número {n2} é o maior!")
    if n3 > n1 and n3 > n2:
        return (f"O número {n3} é o maior!")
    else: 
        "Digite um número válido!"
    
n1 = int(input("Digite o 1º número: "))
n2 = int(input("Digite o 2º número: "))
n3 = int(input("Digite o 3º número: "))
res = maior(n1,n2,n3)
print(res)