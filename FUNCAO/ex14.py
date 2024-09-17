def carro (km,l):
   return km / l


km = float(input("Digite os km: "))
l = float(input("Digite os litros: "))
res = carro(km,l)
if  res == 8:
    print("Gasta muito!")
if res > 8 and res < 15:
    print("Econômico!")
if res == 15:
    print("Super econômico!")


