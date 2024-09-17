## Matriz 4x4 com zeros
## Inicializar e preencher matriz

#while#
l = 4
c = 4
matriz = []
i = 0
while i < l:              # 1º while preenche as linhas da matriz definida na var L 
    linha = []            # Criar a linha
    j = 0                 # Contador do while para preencher as colunas
    while j < c :
        linha.append(0)   # Preenche a coluna com L
        j += 1
    matriz.append(linha)  # Adiciona alinha gerada na matriz
    i += 1
x = 0
while x < len(matriz):
    print(matriz[0])
    x += 1

#for#

matriz = []
for lin in range(4):
    linha = []
    for col in range(4):
        linha.append(1)
    matriz.append(linha)
for linha in matriz:
    print(linha)
    
