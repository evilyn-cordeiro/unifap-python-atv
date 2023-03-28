# Leia 4 valores inteiros A, B, C e D. 
# A seguir, se B for maior do que C 
# e se D for maior do que A, 
# e a soma de C com D for maior que a soma de A e B 
# e se C e D, ambos, forem positivos e se a variável A for par escrever a mensagem "Valores aceitos",
# senão escrever "Valores nao aceitos".

# -------------------------------------

# Entrada
# Quatro números inteiros A, B, C e D.

# Saída
# Mostre a respectiva mensagem após a validação dos valores.

# -------------------------------------

A, B, C, D = input().split()

A = int(A)
B = int(B)
C = int(C)
D = int(D)

soma_cd = C + D
soma_ab = A + B


if B > C and soma_cd > soma_ab and C > 0 and D > 0 and A%2 == 0:
  print('Valores aceitos')
else:
  print('Valores nao aceitos')
