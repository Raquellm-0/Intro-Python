matriz = []
l = 4
c = 4
i = 0
while i < l:
    linha = []
    j = 0
    while j < c:
        print(f"LIN- {i} COL- {j}")
        num = int(input(f"Digite um número: "))
        linha.append(num)
        j += 1
    matriz.append(linha)
    i += 1

x = 0
while x < len(matriz):
    print(matriz[x])
    x += 1
