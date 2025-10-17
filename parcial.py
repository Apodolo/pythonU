#Camilo Avila - Danilo Rodriguez

# Ejercicio #7

# Le pedimos la palabra o frase al usuario para luego mostrarla alreves

palabra = str(input("Ingresa una palabra "))    
invertido = ""

# Utilizamos un bucle for para invertir la palabra o la frase =

for invertir in palabra:
    invertido = invertir + invertido

# imprimimos el la palabra o frase alreves

print(invertido)


# Ejercicio 8

# Le pedimos al usuario que ingrese los datos de las 2 matrices
print("Ingresa los valores para la matriz 1")

matriz1 = [
    [int(input("ingrese el elemento para 1x1"))], [int(input("ingrese el elemento para 1x2"))],
    [int(input("ingrese el elemento para 2x1"))], [int(input("ingrese el elemento para 2x2"))]
]
print("Ingrese los valores para la matriz 2")
matriz2 = [
    [int(input("ingrese el elemento para 1x1"))], [int(input("ingrese el elemento para 1x2"))],
    [int(input("ingrese el elemento para 2x1"))], [int(input("ingrese el elemento para 2x2"))]
]

#Hacemos el procedimiento para la suma de las 2 matrices

suma = [
    [matriz1[i][j] + matriz2[i][j] for j in range(2)]
    for i in range (2)
]

#Aqui mostramos el resultado de la suma de las 2 matrices
print("El resultado de la suma de las 2 matrices es: ")
for imprimir in suma :
    print(imprimir)