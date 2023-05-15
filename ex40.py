# número para se analizar os divisores
num = int(input())
# número máximo para se analisar
max_num = int(input())
# número min para se analisar
min_num = int(input())

# estrutura de repetição quando se sabe quantas
# vezes irá se repetir a sequência
for i in range(min_num, max_num + 1):
    if i % num == 0 and i % 2 == 0:
        print(i, end = '')