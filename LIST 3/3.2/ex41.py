while True:
    r1 = int(input("Digite o R1: "))
    r2 = int(input("Digite o R2: "))
    if r1 == 0 or r2 == 0:
        print("Fim do programa!")
        break
    else:
        R = (r1 * r2) / (r1 + r2)
        print(f"Resistência: {R:.2f}\n")