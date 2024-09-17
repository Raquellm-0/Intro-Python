dis = float(input("Digite a distância em km: "))
lit = float(input("Digite a quantidade de litros de gasolina: "))
cal = dis / lit

if cal < 8:
   print("Venda o carro!")
elif cal >= 8 and cal <= 14:
     print("Econômico!")
else:
   cal > 14
   print("Super econômico!")