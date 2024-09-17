peso = float(input("Digite seu peso: "))
h = float(input("Digite su altura: "))
imc = peso / (h * h)
if imc <= 18.5:
    print("Abaixo do peso!")
elif imc >= 18.6 or imc <= 29.9:
    print("Saudável!")
elif imc >= 25.0 or imc <= 29.9:
    print("Peso em ecesso!")
elif imc >= 30.0 or imc <= 34.9:
    print("Obesiddade grau 1!")
elif imc >= 35.0 or imc <= 39.9:
    print("Obesidade grau 2 (severa)!")
else:
    print("Obesidade grau 3 (mórbida)!")

    