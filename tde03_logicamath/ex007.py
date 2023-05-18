# beecrowd | 1471
# Mergulho
# Maratona de Programação da SBC  Brasil
# Timelimit: 1

aposta = set(map(int, input().split()))
sorteados = set(map(int, input().split()))
acertos = len(aposta.intersection(sorteados))
if acertos == 3:
      print('terno')
elif acertos == 4:
      print('quadra')
elif acertos == 5:
      print('quina')
elif acertos == 6:
      print('sena')
else:
      print('azar')