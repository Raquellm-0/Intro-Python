cont = 0
for cont in range(1):
    print("• BEBÊ:")
    nome_bebe = str(input("Digite nome do bebê: "))
    data_bebe = int(input("Digite data de nascimento do bebê: "))
    peso = float(input("Digite o peso de nascimento do bebê: "))
    altura = int(input("Digite a altura do bebê em cm: "))
    mae_bebe = str(input("Digite o nome da mãe do bebê: "))
    medico_bebe = str(input("Digite o nome do médico que fez o parto do bebê: "))
    print("• MÃE: ")
    nome_mae = str(input("Digite nome da mãe: "))
    endereco = str(input("Digite o endereço da mãe: "))
    telefone = int(input("Digite o número de telefone da mãe: "))
    data_mae = int(input("Digite a data de nascimento da mãe: "))
    print("• MÉDICO: ")
    nome_medico = str(input("Digite o nome do médico: "))
    crm = int(input("Digite a CMR do médico: "))
    telefone_medico = int(input("Digite o número de telefone do médico: "))
    especialidade = str(input("Digite a especialidade do médico: "))

print("\n\n• INFORMAÇÕES DO BEBÊ: ")
print(nome_bebe)
print(data_bebe)
print(peso)
print(altura)
print(mae_bebe)
print(medico_bebe)
print("\n• INFORMAÇÕES DA MÃE: ")
print(nome_mae)
print(endereco)
print(telefone)
print(data_mae)
print("\n• INFROMAÇÕES DO MÉDICO: ")
print(nome_medico)
print(crm)
print(telefone_medico)
print(especialidade)