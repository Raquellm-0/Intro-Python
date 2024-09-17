area = float(input("Digite a área a ser pintada: "))
lata = 18 * 6

print("Cobertura por lata: ",lata)
total_latas = area / lata
print("Total de latas: ",total_latas)
preco_lata = 25
total_preco_lata = preco_lata * total_latas
print("Valor total utilizando latas: ",total_preco_lata)

galao = 3.6 * 6
print("Cobertura por galão: ",galao)
total_galao = area / galao
print("Total de galões: ",total_galao)
preco_galao = 80
total_preco_galao = preco_galao * total_galao
print("Valor total utilizando galões: ",total_preco_galao)