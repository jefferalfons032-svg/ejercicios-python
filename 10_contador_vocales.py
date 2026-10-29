
frase = "FC 25 ES LO MISMO QUE FC 27 XD"
vocales = 0

for letra in frase.lower():
    if letra in "aeiou":
        vocales += 1

print("La cantidad de vocales es:", vocales)
