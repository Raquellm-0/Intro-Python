qnt = float(input("Digite seu kvh gastos por mês: "))
dia = qnt / 30
print("Consumo diario é de: ",dia)
sol = 5.4 #BH#
potencia = dia / (0.75 * sol ) 
print("A potência é de: ",potencia)
painel = float(input("Digite a potencia, em volts, do seu painel, fotovoltaico, escolhido: "))
total = (potencia / painel) * 1000
print(f"A quantidade necessaria sua residência são de {total:.1f} placas solares, fotovoltaicas: ")
