escolha = str(input("Digite soma, diferença, produto ou divisão:"))
if escolha == 'soma':
    n1 = float(input("Digite 1º número: "))
    n2 = float(input("Digite 2º número: "))
    soma = n1 + n2
    print("Resultado: ",soma)
if escolha == 'diferença':
    n1 = float(input("Digite 1º número: "))
    n2 = float(input("Digite 2º número: "))
    n1 > n2 or n2 > n1
    dif = n1 - n2 or n2 - n1
    print("Resultado: ",dif)
if escolha == 'produto':
    n1 = float(input("Digite 1º número: "))
    n2 = float(input("Digite 2º número: ")) 
    pro = n1 * n2   
    print("Resultado: ",pro)
if escolha == 'divisão':
    n1 = float(input("Digite 1º número: "))
    n2 = float(input("Digite 2º número: "))
    if n1 > 0 and n2 > 0:
      div = n1 / n2
      print("Resultado: ",div)  
    else:
        print("Denominador não pode ser zero!!")  

       