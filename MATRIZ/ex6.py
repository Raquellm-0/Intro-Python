x = [[40,30,20],[17,16,14],[19,15,18]]
y = [[31,32,33],[21,22,23],[12,13,19]]

z = []
i = 0

while i < len(x):
    linhaz = []
    j = 0  ##colunas
    while j < len(x[i]):
        soma = x[i][j] + y[i][j]
        linhaz.append(soma)
        j += 1
    z.append(linhaz)
    i += 1

i = 0
while i < len(x):
    print(x[i])
    i += 1

print()
i = 0
while i < len(y):
    print(y[i])
    i += 1

print()   
i = 0
while i < len(z):
 print(z[i])
 i += 1