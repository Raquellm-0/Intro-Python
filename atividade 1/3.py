pedido = int(input("\n• Deseja realizar um pedido?\n 1-Sim\n 2-Não\n R: "))
if pedido == 2:
   print("\n!!Agradecemos a atenção, tente novamente!!")
res2 = 0
while pedido == 1:
    prato2 = int(input("\n• CARDÁPIO: \n 1- Macarrão- R$33.00 \n 2- Carreteiro- R$26.00 \n 3- Batata Recheada- R$36.00 \n 4- Lazanha- R$25.00 \n 5- Strogonoff- R$30.00 \n 6- Carne oa Molho- R$40.00\n 7- Porção de Batata Frita- R$26.00 \nDigite o respectivo número do seu prato: "))
    qnt2 = int(input("\n• Digite a quantidade: "))
    pedido = int(input("\n• Deseja realizar outro pedido?\n 1-Sim\n 2-Não\nR: "))
    match prato2:
      case 1:
        valor2 = 33.00
        res2 = valor2 * qnt2
      case 2:
        valor2 = 26.00
        res2 =  valor2 * qnt2
      case 3:
        valor2 = 36.00
        res2 = valor2 * qnt2
      case 4:
        valor2 = 25.00
        res2 = valor2 * qnt2
      case 5:
        valor2 = 30.00
        res2 = valor2 * qnt2
      case 6:
        valor2 = 40.00
        res2 = valor2 * qnt2
      case 7:
        valor2 = 26.00
        res2 = valor2 * qnt2
   

gor = int(input("\n• Deseja atribuir mais 10% do valor do seu prato como gorjeta? \n 1- Sim\n 2- Não\nR:"))   
if gor == 1:
    gor = 0.10 * res2
    total = gor + res2
    print("\nValor total a pagar é R$",total)
elif gor == 2:
  print("\nValor total a ser pago R$",res2)
else:
    print("\n!!Número Inválido, tente novamente!!")

