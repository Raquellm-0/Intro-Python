valor = float(input("Digite o valor do produto: "))
estado = str(input("DIgite o estado destino do produto: "))
if estado == 'mg':
    v = 0.07 * valor
    vf = valor + v
    print("Preço final: ",vf)
elif estado == 'sp':
    v = 0.12 * valor
    vf = valor + v
    print("Preço final: ",vf)    
elif estado == 'rj':
    v = 0.15 * valor
    vf = valor + v
    print("Preço final: ",vf)
elif estado == 'ms':
    v = 0.08 * valor
    vf = valor + v
    print("Preço final: ",vf)
else:
    print("Estado inválido!!")
