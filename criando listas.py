##CRIANDO LISTA##
#len: tamanho da lista
numeros = [21,28,15,33]
print(len(numeros))

# #slice: fatiamento de lista
numeros = [10,9,5,8,7,3]
print(numeros)
print(numeros[2:5])

# #append: adiciona elemento ao final da lista
numeros = [21,28,15,33]
print(numeros)
numeros.append(49.90)
numeros.append(56)
print(numeros)

# #pop: remove último item da lista
numeros = [21,28,15,33,27]
print(numeros)
numeros.pop()
print(numeros)

#isert: insere elemento em uma posição específicada lista
numeros = [21,98,15,33,48,90,56,27]
print(numeros)
numeros.insert(2,63)
print(numeros)

#index: retorna o índice do primeiro elemento com o valor especificado
numeros = [21,98,15,33,48,90,56,27]
print(numeros)
print(numeros.index(56))

#sort: ordena a lista em ordem crescente
numeros = [21,98,15,33,48,90,56,27]
numeros.sort()
print(numeros)

#sort(reverse=True): ordena a lista em ordem decrescente
numeros = [21,98,15,33,48,90,56,27]
numeros.sort(reverse=True)
print(numeros)

#remove: remove valor selecionado 
numeros = [21,98,15,33,48,90,56,27]
numeros.remove(33)
print(numeros)

#min: menor número da lista
numeros = [21,98,15,33,48,90,56,27]
print(min(numeros))

#max: maior número da lista
numeros = [21,98,15,33,48,90,56,27]
print(max(numeros))

#sum: soma dos números
numeros = [21,98,15,33,48,90,56,27]
print(sum(numeros))

#media da lista 
numeros = [21,98,15,33,48,90,56,27]
media = sum(numeros) / len(numeros)
print(f"{media:.2f}")

#range: contagem
for i in range(10):
    print(i)

#pares ou ímpares#
for i in range(3,20,3):
    print(i)



numeros = [2.3,3,7.9,7.4,6.8,6,4]
numeros.pop()
numeros.pop()
print(numeros)

numeros.append(49)
numeros.append(56)
numeros.append(99)
print(numeros)

numeros.insert(6,66)
print(numeros)

numeros.remove(6.8)
print(numeros)

print(len(numeros))

print(sum(numeros))

media = sum(numeros) / len(numeros)
print(f"{media:.2f}")

numeros.sort()
print(numeros)

numeros.sort(reverse=True)
print(numeros)

print(max(numeros))

print(min(numeros))