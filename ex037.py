# beecrowd | 1070
# Seis Números Ímpares
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1

num = int(input())
i = 0

if (num % 2 == 0):
    num += 1
    print(num)
else:
    print(num)

for i in range(1,6):
    num +=2
    print(num)
    
