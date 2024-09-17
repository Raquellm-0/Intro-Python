try:
    n1 = float(input("Digite o 1º número: "))
    n2 = float(input("Digite o 2º número: "))
    n3 = float(input("Digite o 3º número: "))
    if n1 > n2 > n3:
      print("Está em ordem decrescente!!")
    else:
     print("Não está em ordem decrescente!!") 
except:
  print("Não está em ordem decrescente!!")  