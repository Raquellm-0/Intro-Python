custo = float(input("Digite o custo de fábrica: "))
if custo <= 12000:
    c = 0.05 * custo
    cst = custo + c
    print("Custo: ",cst)
elif custo > 12000 and custo< 25000:
    c = ((0.10 * custo) * 0.15) + custo
    print("Custo: ",c)
elif custo > 25000:
    c = ((0.15 * custo) * 0.20) + custo
    print("Custo: ",c)
else:
    print("Valor inválido!")
