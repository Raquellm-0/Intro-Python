cont = 0

while cont >= 0:
    num = int(input("Digite um número ou 0 para finalizar: ")) 
    if num % 2 == 0 and num != 0:
       print(num)
       print("Par!")
       cont = cont + 1
    elif num % 2 == 1 and num != 0 :
        print(num)
        print("Ímpar!")
        cont = cont + 1
    elif num == 0:
        print("Total de dados lidos: ",cont)
