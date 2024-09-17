def argnomeados(param1,**kwargs):
    imp = kwargs['imposto']
    res = param1 * imp / 100
    res = res + kwargs['valor']
    res = res + (res * kwargs['porcentagem']) / 100
    txt = f'{kwargs["n"]} deve {res}'
    return txt
    # print(param1)
    # print(kwargs['imposto'])

x = argnomeados(1000,imposto = 20, valor = 40, porcentagem = 50, n = "nome")
print(x)