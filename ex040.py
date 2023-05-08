# beecrowd | 1036
# Fórmula de Bhaskara
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
import math

A = float(input())
B = float(input())
C = float(input())
D = (B ** 2) - (4 * A * C)

if (D <= 0 or A==0):
  print('Impossível calcular')
else :
  D = math.sqrt(D)
  R1 = (-B+D) / (2*A)
  R2 = (-B-D) / (2*A)
  print('R1 = %5f' %R1)
  print('R2 = %5f' %R2)
