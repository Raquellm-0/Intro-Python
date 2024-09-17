try:
    n1 = int(input("Digite o 1º número: "))
    n2 = int(input("digite o 2º número: "))
    n3 = float(input("Digite um número real: "))
    p = n2 / 2
    pr = p * n1
    print("Valor do produto do primeiro número com a metade do segundo:",pr)
    tri = n1 * 3
    soma = tri + n3
    print("Valor da soma do triplo do primeiro número com o terceiro: ",soma)
except:
    print("Digite um valor válido!")