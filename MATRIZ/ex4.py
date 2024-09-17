matriz = []
try:
    for lin in range(8):
        linha = []
        for col in range(8):
            linha.append(1)
        matriz.append(linha)
    for linha in matriz:
        print(linha)
    i = 0
    for i in range(1):   
        l = int(input("Digite a LINHA que deseja marcar: "))
        c = int(input("Digite a COLUNA que deseja marcar: "))
        matriz[l][c] ='X'
        for linha in matriz:
            print(linha)
    if l < 0 and l > 8 and c < 0 and c > 8:
     print("Digite um valor válido!")
except:
     print("Digite um valor válido!")






##WHILE##
# while True:
#     op = input("Deseja marcar um 'X'? \n 0- Sim\n 1- Não\nR: ")
#     if op == 1:
#         break
#     if op == 0:
#      linha = int(input("Digite a LINHA desejada: "))
#      coluna = int(input("Digite a COLUNA desejada: "))

