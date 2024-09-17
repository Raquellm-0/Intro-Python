valor = float(input("Digite o valor ganho por hora: "))
hora = float(input("Digite o número de horas trabalhadas no mês: "))
cll = valor * hora
inss = 0.08 * cll
sind = 0.05 * cll
ir = 0.11 * cll 
salario_bruto = cll - inss - sind - ir
print("Slário bruto: ",salario_bruto)
salario_liquido = salario_bruto - inss - sind - ir
print("Salário Líquido: ",salario_liquido)
