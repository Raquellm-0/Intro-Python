def volume(r,h,pi):
    return pi * (r * r) * h

pi = 3.141592
r = int(input("Digite o raio do cilíndro: "))
h = int(input("Digite a altura do cilíndro: "))
res = volume(r,h,pi)
print(res)
