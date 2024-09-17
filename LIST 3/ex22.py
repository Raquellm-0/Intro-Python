nota = 0
i = 0
soma = 0
while i >= 0:
   nota = int(input("Digite uma nota de aprovação ente 0 e 10 ou 11 para finalizar: "))
   if nota != 11:
    soma = soma + nota
    i = i + 1
media = soma / nota
print("Média é de: ",media)
#incompleto