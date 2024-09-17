def temperatura(graus):
    return graus * (9.0 / 5.0) + 32.0
graus = float(input("Digite os graus Celsius: "))
res = temperatura(graus)
print(res)
