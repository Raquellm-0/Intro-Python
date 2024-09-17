try:
    a = float(input("Digite sua altura: "))
    s = str(input("Digite seu sexo, homem ou mulher: "))
    if s == 'mulher':
     m = (62.1 * a) - 44.7
     print("Seu peso ideal, feminino, é de: ",m)
    else:
     h = (72.7 * a) - 58
     print("Seu peso ideal, masculino, é de: ",h)    
except:
    print("Digite um valor válido!")