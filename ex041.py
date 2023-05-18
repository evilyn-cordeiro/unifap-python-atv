# Faça um programa que receba um número inteiro 
# positivo qualquer e mostre a soma
# de todos os seus divisores ímpares.

# receptor do número inteiro
# int_num = int(input())

# o que define um número ímpar?
# caso um número seja dividido por 2 o resto seja diferente de 0 então ele é considerado um número ímpar
# num % 2 != 0

# como classificar um dívisor de um número?
# se um número ao dividir um número ele ser igual a 0 então ele é divisor de outro
# num % x = 0

# como saber todos os divisores de um número?

# 100 100
# 100 50
# 100 25
# 100 20
# 100 10
# 100 5
# 100 2
# 100 1
num = int(input())

for i in range(1, num + 1):
    # if num % i == 0:
    #   if i % 2 != 0:
    if num % i == 0 and i % 2 != 0:
        print(i) 

