def tempo(n1,n2,n3):
    return  (n1 * 60 * (60) + (n2 * 60) + n3)
n1 = float(input("Digite as horas: "))
n2 = float(input("Digite os minutos: "))
n3 = float(input("Digite os segundos: "))
res = tempo(n1,n2,n3)
print(f"Segundos",res)

