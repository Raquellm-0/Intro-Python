i = imc = f = m = h = 0
idade = int(input("Idade: "))
sexo = input("Sexo, digite 'F' para feminino ou 'M' para masculino: ")
peso = float(input("Peso: ")) 
altura = float(input("Altura: "))
mais_velho = idade
mais_novo = idade
mais_alto = altura
mais_baixo = altura
maior_peso = peso
while i <= 3:  #25
    if idade > mais_velho:
        mais_velho = idade
    if idade < mais_novo:
        mais_novo = idade
    if altura > mais_alto:
        mais_alto = altura
    if altura < mais_baixo:
        mais_baixo = altura
    if peso > maior_peso:
        maior_peso = peso
    altura += altura
    imc = peso / (altura * altura)
    if sexo == "F" or sexo == "f":
        f += 1
    if sexo == "M" or sexo == "m":
        m += 1
    i += 1
    idade = int(input("Idade: "))
    sexo = input("Sexo, digite 'F' para feminino ou 'M' para masculino: ")
    peso = float(input("Peso: ")) 
    altura = float(input("Altura: "))
print("Mais velho:",mais_velho)
print("Mais novo: ",mais_novo)
print("Mais alto: ",mais_alto)
print("Mais baixo: ",mais_baixo)
print("Maior peso: ",maior_peso)
pf = (f / i) * 100
pm = (m / i) * 100
mediah = h / i
mediaimc = imc / i
print("Porcentagem do sexo feminino: ",pf)
print("Porcentagem do sexo masculino: ",pm)
print("Média das alturas: ",mediah)
print("Média dos IMC's: ",mediaimc)