av = int(input("Digite o número de avaliações do estudante: "))
media = 0
for i in range(av):
    nota = int(input("Nota: "))
    media = media + nota
media = media / av
print("Média: ",media)
