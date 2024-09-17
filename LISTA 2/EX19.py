n1 = float(input("Digite o valor da 1º nota: "))  
n2 = float(input("Digite o valor da 2º nota: "))  
n3 = float(input("Digite o valor da 3º nota: "))  

mult = ((n1 * 1) + (n2 * 1) + (n3 * 2)) * 10

media = mult / 4

if media >= 60:
   print("Aprovado!! ",media)
else: 
   print("Reprovado!! ",media)  