lab = float(input("Digite nota de laboratório: "))
ava = float(input("Digite nota de avaliação: "))
exa = float(input("Digite nota do exame: "))

media = ((lab * 2) + (ava * 3) + (exa * 5)) / 10

if media > 0 and media < 2.99:
   print("Reprovado ",media)
elif media > 3 and media < 5.99:
   print("Recuperação ",media)
else: 
   print("Aprovado ",media)      