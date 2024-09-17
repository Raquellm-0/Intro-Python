def meses(i):
    if i == 1:
        return "janeiro"
    if i == 2:
        return "fevereiro"
    if i == 3:
        return "março"
    if i == 4:
        return "abril"
    if i == 5:
        return "maio"
    if i == 6:
        return "junho"
    if i == 7:
        return "julho"
    if i == 8:
        return "agosto"
    if i == 9:
        return "setembro"
    if i == 10:
        return "outubro"
    if i == 11:
        return "novembro"
    if i == 12:
        return "dezembro"
    else:
        return "Digite um número válido!"
    
d = int(input("Digite o dia: "))
i = int(input("Digite o número do mês: "))
a = int(input("Digite o ano: "))
ano = meses(i)
print(f"Dia {d} de {ano} de {a}!")
