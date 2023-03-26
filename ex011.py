l = int(input('Largura: '))
h = int(input('Altura: '))

# area
a = l * h
litros_de_tinta = a / 2

print('A área do espaço é {}m² e precisa  de {}L de tinta para pintar esse mesmo espaço!'.format(a, litros_de_tinta))