def notas(n1,n2,n3,l):
    if l == 1:
        return (n1 + n2 + n3) / 3
    if l == 2:
        return (n1 + n2 + n3) / 10
    else:
        "Digite um número válido!"
        
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
l = int(input("Letra\n 1- A\n 2- P\nDigite a respectiva letra: "))
res = notas(n1,n2,n3,l)
print(f"Média: {res:.2f}")
