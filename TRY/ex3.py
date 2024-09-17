#Exercício 6 da lista 2#
try: 
    turno = int(input("•Turno:\n 1- Matutino\n 2- Vespertino\n 3- Noturno\nDigite o respectivo número do turno em que você estuda: "))
    if turno == 1:
        print("Bom Dia!")
    elif turno == 2:
        print("Boa Tarde!")
    elif turno == 3:
        print("Boa Noite!")
except:
    print("Valor Inválido!")
