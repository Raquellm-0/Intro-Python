try:
    num = int(input("Digite um número inteiro: "))
    if num > 0:
     aq = num * 2
     print("Ao quadrado: ",aq)
     print("Raíz:",num**0.5)
    else:
      print("Número negativo!!")  
except:
    print("Digite um valor válido!")
