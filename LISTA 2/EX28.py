idade = int(input("Digite sua idade: "))
tempo = float(input("Digite seu tempo de serviço (em anos): "))
if idade >= 65 and tempo >= 30:
    print("Pode se aposentar!!")
elif idade >= 60 and tempo >= 25:
    print("Pode se aposentar!!")
else:
    print("Não pode se aposentar!!")    
