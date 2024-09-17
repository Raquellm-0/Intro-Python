alunos = 50
 
qfas170 = 0
qmsfb = 0
 
for _ in range (alunos):
    matricula = input("Digite a matrícula do aluno: ")
    sexo = input("• SEXO DO ALUNO(A):\n M- Masculino\n F- Femnino\nDigite o sexo do aluno(a): ")
    altura = float(input("Digite a altura do aluno em centímetros: "))
    fisico = int(input("• STATUS FíSICO DO ALUNO:\n 1- Bom\n 2- Regular\n 3- Ruim\nDigite o status fisico do aluno(a): "))
    if sexo.upper() == 'F' and altura > 170:
        qfas170 += 1
         
    if sexo.upper() == 'M' and fisico == 1:
        qmsfb += 1
       
       
pmsb = (qmsfb / (alunos / 2)) * 100
print("A quantidade de alunas no sexo feminino com altura superior a 170cm : ", qfas170)
print("A porcentagem de alunos do sexo masculino com status fisico bom: {:.2f}%".format(pmsb))