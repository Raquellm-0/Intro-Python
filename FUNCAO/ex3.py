def num(n):
    if n > 0:
        return "1"
    if n < 0:
        return "-1"
    if n == 0:
        return "0"
    else:
        "Digite um número válido!"
        
n = int(input("Digite um número: "))
res = num(n)
print(res)
