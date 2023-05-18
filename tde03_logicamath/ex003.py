# beecrowd | 1329
# Cara ou Coroa
# Maratona de Programacao da SBC 2004, Warm-Up  Brasil
# Timelimit: 1
while True:
      n = int(input())
      if n == 0:
            break
      resultados = list(map(int, input().split()))
      mariav = resultados.count(0)
      joaov = resultados.count(1)
      print("Maria venceu {} vezes e João venceu {} vezes ".format(mariav, joaov))