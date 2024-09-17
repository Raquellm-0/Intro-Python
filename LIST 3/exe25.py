media = 0
i = 0
fim = False
while fim == False:
    idade = int(input("Digite sua idade ou zero para finalizar: "))
    if idade == 0:
        fim = True
        if idade > 0:
          media = media + idade
          total = media / idade
print(f"A idade média é de:{media:.1f}")
#incompleto