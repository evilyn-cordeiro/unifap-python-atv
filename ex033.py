nome = input()
salario_fixo = float(input())
montante_total = float(input())

porcentagem = montante_total * (15/100)
novo_salario = porcentagem + salario_fixo

print('TOTAL =  R$ %.2f' %novo_salario)
