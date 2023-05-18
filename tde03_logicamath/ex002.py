# beecrowd | 1171
# Frequência de Números
# Adaptado por Neilor Tonin, URI  Brasil
# Timelimit: 1
import collections
n = int(input())
inputs = []

for i in range(n):
    valor = int(input())
    inputs.append(valor)

count = collections.Counter(inputs)
for valor, count in sorted(count.items()):
    print(f'{valor} aparece {count} vez(es)')