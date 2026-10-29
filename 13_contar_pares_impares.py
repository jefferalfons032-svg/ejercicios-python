
numeros = [2, 5, 8, 3, 10, 7, 4, 9]

pares = 0
impares = 0

for numero in numeros:
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print("La cantidad de numeros pares fueron :", pares)
print("La cantidad de numeros impares fueron :", impares)
