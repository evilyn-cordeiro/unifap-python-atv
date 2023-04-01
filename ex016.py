# insira o nome de cada aluno
# -----------------------------
# insira a nota de cada bimestre (4 bimestres)
# -----------------------------
# média de cada aluno
# -----------------------------
# moda de todas as notas finais
# -----------------------------
# mediana de todas as notas finais

qtd_alunos = int(input('Quantos alunos tem na turma? '))
contador = 0
alunos = []
notas = []

while contador != qtd_alunos:
    nome = input(f'Informe o nome do {contador+1}° aluno: ')
    alunos.append(nome)
    contador += 1
    notas_aluno = []
    j = 0
    while j < 4: # 4 bimestres
        nota = float(input(f"Informe a nota do {j+1}º bimestre de {nome}: "))
        notas_aluno.append(nota)
        j += 1
    notas.append(notas_aluno)
    j += 1

# Calculando a média de cada aluno
medias = []
for notas_aluno in notas:
    media = sum(notas_aluno) / len(notas_aluno)
    medias.append(media)

# Calculando a moda e mediana de todas as notas finais
notas_finais = [sum(notas_aluno) for notas_aluno in notas]
moda = max(set(notas_finais), key=notas_finais.count)
notas_finais.sort()
tamanho = len(notas_finais)
mediana = (notas_finais[tamanho//2] + notas_finais[-(tamanho//2+1)]) / 2

# Exibindo resultados
print("\nMédias dos alunos:")
print('---------------------------')
for i, nome in enumerate(alunos):
    print(f"{nome}: {medias[i]}")
print(f"Média das notas finais: {sum(notas_finais)/tamanho}")
print('---------------------------')
print(f"Moda das notas finais: {moda}")
print('---------------------------')
print(f"Mediana das notas finais: {mediana}")