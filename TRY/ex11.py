try:
    id = int(input("Digite sua idade: "))
    if id >= 5 and id < 12:
        print("Nadador(a) Infantil!")
    if id == 12 and id <= 17:
        print("Nadador(a) Juvenil!")
    if id >= 18:
        print("Nadador(a) Sênior!")
    if id < 5:
        print("Não pode nadar ainda!")
except:
    print("Digite um valor válido!")

