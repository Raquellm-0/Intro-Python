idade = int(input("Digite sua idade: "))
if idade >= 5 and idade <= 12:
    print("Infantil")
elif idade >= 12 and idade <= 17:
    print("Juvenil")
elif idade > 18:
    print("Sênior")
else:
    print("Não possui idade para nadar!")
