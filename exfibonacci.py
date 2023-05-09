# mostre a série Fibonacci até a posição informada pelo usuário
pos = int(input('Número: '))
# valor atual da sequência de fibonacci
fib_novo = 1
# valor anterior referente a sequência de fibonacci
fib_ant = 0

for i in range(pos):
  # apresenta o primeiro valor da sequência de fibonacci --  iniciando em 1
  print(fib_novo)
  # acrescenta ao valor anterior da sequência
  fib_novo += fib_ant
  # atribui ao valor anterior o novo valor (1) menos o valor anterior(0)
  fib_ant = fib_novo - fib_ant

# finaliza o programa quando o valor a ser incrementado chega ao fim
print('Fim do programa')

# '''

# calcule a possibilidade de uma pessoa ganhar na Mega sena fazendo uma aposta mínima

