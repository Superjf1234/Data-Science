import numpy as np

arreglo = np.array([1, 2, 3, 4, 5])

print(arreglo)
print(type(arreglo))

arreglom = np.array([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]])

print(arreglom)
print(type(arreglom))

arreglo1 = np.array([1, 2, 3, 4, 5])
arreglo2 = np.array([6, 7, 8, 9, 10])


# Suma
suma = arreglo1 + arreglo2

print("Suma de Arreglo es", suma)

# Resta

resta = arreglo1 - arreglo2
print("La Resta de Arreglo es", resta)

# Multiplicacion

multi = arreglo1 * arreglo2
print("La Multiplicacion de Arreglo es", multi)

# Division

div = arreglo1 / arreglo2
print("La division de Arreglo es", div)

# Matriz de Ceros

zerosa = np.zeros((3, 4))

print(zerosa)

# Matriz de Unos

unoa = np.ones((3, 4))

print(unoa)

# Arange

rango = np.arange(0, 10, 1)

print(rango)

arreglo5 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])

print(arreglo5)

print(arreglo5[2, 4])

valoresx = arreglo2 + 2

print(valoresx)

# funciones estadistica en Numpy

suma2 = np.sum(valoresx)

# Unidimensional
print(suma2)

# Multi - Dimensional
suma3 = np.sum(arreglo5)
print(suma3)

# Exponencial

exp2 = np.exp(arreglo5)
print(exp2)

# Raiz

raiz = np.sqrt(valoresx)

print(raiz)

# Mean y STD

mean = np.mean(arreglo5)

print(mean)

std = np.std(arreglo5)
print(std)

# Concatenar

concatenar = np.concatenate((arreglo1, arreglo2))

print(concatenar)

# Convertir reshape

arreglo43 = [[6, 7, 8, 9, 10, 12]]

cambio = np.reshape(arreglo43, (3, 2))

print(cambio)


arreglo66 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [22, 33, 44, 55, 66]])

cambio2 = np.reshape(arreglo66, (3, 5))

print(cambio2)

# Numeros aleatorios

numeros = np.random.rand(6, 3)

print(numeros)
