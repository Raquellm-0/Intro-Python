somaq = soma = 0
i = 1
while i <= 100:
    somaq += i ** 2
    soma += i
    i += 1   
dif = (soma ** 2) - somaq
print(dif)


##FOR##
somaq = soma = 0
for i in range(1,11):
    somaq += i ** 2
    soma += 1
print((somaq ** 2) - soma)