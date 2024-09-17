qnt = int(input("Digite a quantidade de números a serem lidos: "))
num = []
for i in range(qnt):
     num.append(int(input("Digite um número: ")))

print(max(num))
