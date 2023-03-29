# Leia um valor inteiro, que é o tempo de duração em segundos de um determinado
# evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.

# --------------------------------

# Entrada
# O arquivo de entrada contém um valor inteiro N.

# --------------------------------

# Saída
# Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, conforme exemplo fornecido.

valor = int(input())

horas = (valor // 3600)
minutos = (valor % 3600) // 60
segundos = (valor % 3600) % 60

print('{}:{}:{}'.format(horas, minutos, segundos))