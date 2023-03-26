palavra = input("Digite uma palavra: ")

vogais = "aeiouAEIOU"

contador = 0

for letra in palavra:
    if letra in vogais:
        contador += 1

print("A palavra '{}' tem {} vogais!".format(palavra, contador)) 