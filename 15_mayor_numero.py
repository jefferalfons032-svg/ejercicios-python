
numeros = [12, 45, 8, 67, 23, 90, 34]

mayor = numeros[0]

for numero in numeros:
    if numero > mayor:
        mayor = numero

print("El numero de la lista fue :", mayor)
