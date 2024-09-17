# # lista = []
# # tupla = ()

# # ##Dicionário com chaves{}## -> matriz composta por CHAVES e VALORES
pessoa = {
    'nome':'EU',
    'idade':32,
    'email':'ljjfjkfj@gmail.com',
    'fone':'0000000000'
}
# # print(pessoa['fone'])
# # print(pessoa['idade'])

# ## No LINUX as variáveis, caminhos, estruturas de dados são CASE SENSITIVE -> sensitivo ao caso


# ## DICIONARIO COM CHAVE E VALORES
dicionario = {
    'nome':'EU',
    'idade':18,
    'cidade':'CG',
    'estado':'MS'
}
# # print(type(dicionario))
# # print(dicionario['nome'])
# # print(dicionario['idade'])
# # print(dicionario['cidade'])
# # print(dicionario['estado'])
# # print(dicionario)


empresa = {
    'razaosocial': 'CLARO SA',
    'cidade': 'São Paulo',
    'estado': 'SP',
    'ganhos': 14.6
#      #keys   #values
}
# # print(empresa['estado'])
# # print(empresa['ganhos'])

for item in empresa.keys():  #imprime as chaves
    print(item)

for item in empresa.values(): #imprime os valores
    print(item)

for k, v in empresa.items(): #imprime as chaves e os valores
    print(k, v)
        #or
    print(f"{k} : {v}")
    #k = keys n v = values


#preencher um dicionário vazio
fabrica = {}
n = int(input("Digite a quantidade de alunos a cadastrar: "))
for i in range(n):
    fabrica[f'Aluno{i}'] = input("Digite o nome: ")

for k, v in fabrica.items():
    print(f' {k} : {v}')


#Dicionário com lista
    empresa = {
        'filiais':['Plaza', 'Bosque', 'CG'],
        'socios':{
            'top':'nome',
            'cfo':'nome',
            'cty':'nome',
            'ganho':[{},{}]
        }
    }


#OBJETO EM JS EQUIVALE A UM DICIONÁRIO NO PYTHON
# let pessoa = {
#    'nome':'Raquel',
#    'idade':'17',
#    'cidade':'CG',
#    'estado':'MS'
# };

# document.write(pessoa.nome);#"print"
    

