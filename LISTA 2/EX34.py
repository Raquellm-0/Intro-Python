valor = float(input("Digite valor da venda: "))
if valor >= 100000:
    com = ((0.16 * valor) + 700)
    print("Comissão: ",com)
elif valor < 100000 and valor >= 80000:
    com = ((0.14 * valor) + 650)
    print("Comissão: ",com)
elif valor < 80000 and valor >= 60000:
    com = ((0.14 * valor) + 600)
    print("Comissão: ",com)
elif valor < 60000 and valor >= 40000:
    com = ((0.14 * valor) + 550)
    print("Comissão: ",com)
elif valor < 40000 and valor >= 20000:
    com = ((0.14 * valor) + 500)
    print("Comissão: ",com)
elif valor < 20000:
    com = ((0.14 * valor) + 400)
    print ("Comissão: ",com)
