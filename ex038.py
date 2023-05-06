# beecrowd | 1071
# Soma de Impares Consecutivos I
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1

X = int(input());
Y = int(input());

result = 0

for i in range(Y + 1, X):
    if(i % 2 != 0):
        result += i

print(result);
