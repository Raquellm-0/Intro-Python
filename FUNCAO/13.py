def valorpadrao(quant,valor):
    lista = []
    for i in range(quant):
        lista.append(int(valor))
    return lista

a = int(input("Digite o tamanho da lista: "))
b = input("Digite o valor padrão: ")

result = valorpadrao(a,b)
print(result)