salario = float(input('Informe o salário do funcionário: '))

print('O funcionário receberá um aumento de 15%!')
print('o novo valor será de R${}, ou seja, o aumento foi de R${}'.format(salario + (salario * 15/100), salario * 15/100))
