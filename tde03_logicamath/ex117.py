# beecrowd | 1171
# Frequência de Números
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1

cont = int(input())
dicio = {}

for i in range(cont):
    ev = int(input())

    if not ev in dicio.keys():
        dicio[ev] = 0
    dicio[ev] += 1

print(dicio)
