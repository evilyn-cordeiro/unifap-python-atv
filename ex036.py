# estrutura de repetição

# Entrada: um número inteiro
# Processamento: ler até o usuário informar que não tem mais números, e acumular o maior valor informado.
# saída: mostrar o maior valor informado

num = int(input())
contador = input('Continuar (S/N)?')
max = -1

while contador == '5':
  if num > max:
    max = num