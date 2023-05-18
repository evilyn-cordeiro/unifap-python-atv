# beecrowd | 2164
# Fibonacci Rápido
# Por M.C. Pinto, UNILA BR Brazil
# Timelimit: 1

n = int(input())
fibonacci = float((((1 + 5 * 0.5)/2) * n) - (((1 - 5 * 0.5)/2) * n)) / 5 ** 0.5
print(f'{fibonacci :.1f}')