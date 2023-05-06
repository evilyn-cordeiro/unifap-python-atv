# beecrowd | 1072
# Intervalo 2
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1

# qtd de vezes que o código será aplicado
X = int(input())

# contadores (dentro e fora)
x_in = 0
y_out = 0

for i in range(X):
    n = int(input())
    if(n >= 10) and (n <= 20):
        x_in += 1
    else:
        y_out += 1

print('%.0f in' %x_in)
print('%.0f out' %y_out)