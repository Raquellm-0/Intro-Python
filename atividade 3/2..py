branco = nulo = paulo = joao = pedro = jose = 0
while True:
    voto = int(input("• VOTO:\n 1- José\n 2- Pedro\n 3- João\n 4- Paulo\n 5- Voto nulo\n 6- Voto em branco\n • Ou digite 100 para finalizar a votação\n Digite o número do seu voto: "))
    if voto == 100:
        break
    elif voto == 1:
        jose += 1    
    elif voto == 2:
        pedro += 1   
    elif voto == 3:
        joao += 1
    elif voto == 4:
        paulo += 1               
    elif voto == 5:
        nulo += 1
    elif voto == 6:
        branco += 1          
print(f"José recebeu {jose} votos")
print(f"Pedro recebeu {pedro} votos")
print(f"João recebeu {joao} votos")
print(f"Paulo recebeu {paulo} votos")
print(f"Foram {nulo} votos nulos ")
print(f"Foram {branco} votos em branco ")