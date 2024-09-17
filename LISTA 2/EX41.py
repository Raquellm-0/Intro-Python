a = float(input("Digite 'A': "))
b = float(input("Digite 'B': "))
c = float(input("Digite 'C': "))
if  a > 0:
    d = (b * b) - 4 * a * c
    x1 = (- b + d**0.5) / (2 * a)
    x2 = (- b - d**0.5) / (2 * a)
    print("Valor de x1: ",x1)
    print("valor de x2: ",x2)
else:
    print("Não é equação de 2º grau!!")
