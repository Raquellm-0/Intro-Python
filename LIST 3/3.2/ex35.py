palavra = input("Digite alguma coisa: ").lower()
voagais = ['a','e','i','o','u']
con = 0
vog = 0
for letra in palavra:
    if letra not in voagais:
        con += 1
    if letra in voagais:
        vog += 1
print("Total de consoantes: ",con)
print("Total de vogais: ",vog)