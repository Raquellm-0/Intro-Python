media = qnt = soma =0
codigo = int(input("Digite o código da cidade: "))
veiculo = int(input("Digite a quantidade de veículos de passeio: "))
acidente = int(input("Digite o número de acidentes de trânsito com vítimas: "))
menor = 2001
if(veiculo < menor):
        qnt = qnt + 1
        soma = soma + acidente
menor = veiculo
for cidade in range(4):
    media = media +acidente
    codigo = int(input("Digite o código da cidade: "))
    veiculo = int(input("Digite a quantidade de veículos de passeio: "))
    acidente = int(input("Digite o número de acidentes de trânsito com vítimas: "))
    if (veiculo < menor):
        qnt = qnt + 1
        soma = soma + acidente
        menor = veiculo   
media = acidente / qnt
print(media)