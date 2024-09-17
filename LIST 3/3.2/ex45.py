salc = float(input("Digite o salário: "))
salj = salc / 3
mes = 0
while salj <= salc:
    mes += 1
    salc += salc * 0.02
    salj += salj * 0.05
    print(f"Mês {mes} Aumento Carlos: {salc}")
    print(f"Mês {mes} Aumento João: {salj} ")
print("Quantidade de meses: ",mes)