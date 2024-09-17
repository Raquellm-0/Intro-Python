def imprimir(lista):
    cont = 1
    for item in lista:
        print(f' {cont}- {item} ')
        cont += 1

frutas = ['Abacaxi', 'Manga', 'Uva','Maça']
imprimir(frutas)

def imprimirwhile(lista):
    i = 0
    while i < len(lista):
        print(f' {i+1}- {lista[1]}')
        i +=1

frutas = ['Abacaxi', 'Manga', 'Uva','Maça']
imprimirwhile(frutas)
