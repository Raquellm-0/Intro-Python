preco = float(input("Digite o preço antigo do produto: "))
if preco <= 50:
    np = (0.05 * preco) + preco
    print("Novo preço: ",np)
elif preco > 50 and preco <= 100:
    np = (0.10 * preco) + preco
    print("Novo preço: ",np)
else:
    preco > 100
    np = (0.15 * preco) + preco
    print("Novo preço: ",np)
    