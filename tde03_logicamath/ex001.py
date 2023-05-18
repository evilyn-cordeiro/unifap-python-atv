# beecrowd | 1036
# Fórmula de Bhaskara
# Adaptado por Neilor Tonin, URI  Brasil
import math
a = float(input())
b = float(input())
c = float(input())
d = b * b -4 * a * c
if d <= 0 or a == 0:
  print('Impossível calcular')
else :
  R1 = (-b + math.sqrt(d)) / (2*a)
  R2 = (-b - math.sqrt(d)) / (2*a)
  print('R1 = %.5f' %R1)
  print('R2 = %.5f' %R2)
