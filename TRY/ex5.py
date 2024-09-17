try:
    num = int(input("Digite um número entre 1 e 7: "))
    if num == 1:
        print("Segunda-feria!")
    if num == 2:
        print("Terça-feria!")
    if num == 3:
        print("Quarta-feria!")
    if num == 4:
        print("Quinta-feria!")
    if num == 5:
        print("Sexta-feria!")
    if num == 6:
        print("Sábado!")
    if num == 7:
        print("Domingo!")
    if num >= 8 or num <= 0:
        print("Dia inválido!")   
except:
    print("Digite um valor válido!")
