while True:
    num1 = int(input("Digite o 1º número: "))
    num2 = int(input("Digite o 2º número: "))
    menu = int(input("• ESCOLHA:\n 1- Adição\n 2- Subtração\n 3- Multiplicação\n 4- Divisão\n 5- Fim\nDigite o respectivo número de acordo com sua escolha: "))
    match menu:
      case 1:
        res = num1 + num2
        print("Resultado: ",res)
      case 2:
        res = num1 - num2
        print("Resultado: ",res)
      case 3:
        res = num1 * num2
        print("Resultado: ",res)
      case 4:
        res = num1 / num2
        print("Resultado: ",res)
      case 5:
        print("Programa finalizado!!")
        break
          