def calcula_kwh(pot,tempo):
    consumo = (pot * (tempo/60)) / 1000
    return consumo

banho = calcula_kwh(4400,1800)
print(f'Consumo: {banho:.2f} KWH')

preco = 0.67 * banho
print("Valor do banho: ",preco)
