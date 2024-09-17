def esfera(r,pi):
    return 4 / 3 * pi * (r * r * r)

pi = 3.141592
r = int(input("Digite o raio da esfera: "))
res = esfera(r,pi)
print(res)
