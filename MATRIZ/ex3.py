# matriz = [[1,2,3], [4,5,6], [7,8,9]] 
# nova = []
# i = 0
# j = 0
# for i in range(len(matriz)):
#     linha = []
#     for j in range(len(matriz[i])):
#         x = matriz[i][j]*5
#         linha.append(x)
#     nova.append(linha)


# for x in matriz:
#     print(x)

# print()
# for y in nova:
#     print(y)


##WHILE##
matriz = [[1,2,3], [4,5,6], [7,8,9]] 
nova = []
i = 0
j = 0 
while j < len(matriz):
    linha_nova = []
    while j < len(matriz[i]):
        mult = matriz[i][j] * 5
        linha_nova.append(mult)
        j += 1
    nova.append(linha_nova)
    i += 1

x = 0
while x < len(matriz):
    print(matriz[x])
    x += 1
print()
x = 0
while x < len(nova):
    print(nova[x])
    x += 1



