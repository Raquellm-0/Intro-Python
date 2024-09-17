def calculadora(n1,n2,sim):
    if sim == 1:
        return n1 + n2
    if sim == 2:
        return n1 - n2
    if sim == 3:
        return n1 * n2
    if sim == 4:
        return n1 / n2
    else:
        return "Digite um número válido"
    
n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
sim = int(input("Símbolo\n 1- +\n 2- -\n 3- *\n 4- /\nDigite respectivamente o número do operação desejada: "))
res = calculadora(n1,n2,sim)
print(res)
