valor = float(input("Digite seu salário atual: "))
tempo = int(input("Digite seu tempo de serviço, em anos: "))
if valor <= 500 and tempo <= 1:
    ns = 0.25 * valor
    sn = valor + ns
    print("Salário novo: ",sn)
elif valor > 500 and valor <= 1000 and tempo > 1 and tempo <= 3:
    ns = 0.20 * valor
    sn = valor + ns + 100
    print("Salário novo: ",sn)
elif valor > 1000 and valor <= 1500 and tempo >= 4 and tempo <= 6:
    ns = 0.15 * valor
    sn = valor + ns + 200
    print("Salário novo: ",sn)
elif valor > 1500 and valor <= 2000 and tempo >= 7 and tempo <= 10:
    ns = 0.10 * valor
    sn = valor + ns + 300
    print("Salário novo: ",sn)
elif valor >= 2000 and tempo >= 10:
    sn = valor + 500
    print("Salário novo: ",sn)
else:
    print("Sem direito a um reajuste!")
