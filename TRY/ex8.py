try:
    num = int(input("Digite um número: "))
    if num > 0:
        i = num * 2
        v = num ** 0.5
        print(f"{num} ao quadrado é igual a {i} e sua raíz quadrada é de {v}")
    else:
        print("Valor inválido, tente usar um número positivo!")
except:
    print("Digite um valor válido!")