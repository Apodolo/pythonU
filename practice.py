# Ejercicio #1

a = "hola mundo"
print(a)

# Ejercicio #2

name = input("Ingrese su nombre ")
print(name)

# Ejercicio #3

n1 = int(input("ingrese un numero "))
n2 = int(input("ingrese un numero "))
total = (n1 + n2)
print(total)

# Ejercicio #4

base = int(input("Ingrese la base del triangulo "))
altura = int(input("Ingrese la altura del triangulo "))
area = int((base) * (altura))/2
print(area)

# Ejercicio #5

gradosC = float(input("Ingrese los grados Celsius, para realizar la conversión "))
conversion = ((1.8)*(gradosC)) + 32
print(conversion)

# Ejercicio #6

numpoi = int(input("ingrese un numero para saber si es par o impar "))
if numpoi % 2 == 0:
    print("El numero es PAR")
else:
    print("El numero es IMPAR")

# Ejercicio #7

num1 = input("Ingrese un numero ")
num2 = input("Ingrese un numero ")
num3 = input("Ingrese un numero ")
if num1 > num2 and num1 > num3:
    print("El numero mayor es " + num1)
elif num2 > num1 and num2 > num3:
    print("El numero mayor es " + num2)
else:
    print("El numero mayor es " + num3)

# Ejercicio #8

numy = int(input("Ingresa un numero para saber su cuadrado "))
numcuadrado = (numy**2)
print(numcuadrado) 

# Ejercicio #9
 
numerox = int(input("Ingrese un numero, para saber su tabla de multiplicar "))
for i in range (1, 11):
    print(numerox * i)

# Ejercicio #10

palabra = str(input("Ingresa una palabra "))    
alreves = palabra[::-1]
print(alreves)

# Ejercicio #11

edad = int(input("Ingrese su edad "))

if edad >= 18:
    print("Es mayor de edad ")
else:
    print("Es menor de edad")

# Ejercicio #12

numfac = int(input("Ingrese un numero "))
factorial = 1

for i in range (1, numfac + 1):
    factorial *= i
print(factorial)

# Ejercicio #13

nm1 = float(input("Ingrese un numero")) 
nm2 = float(input("Ingrese un numero "))
nm3 = float(input("Ingrese un numero "))
nm4 = float(input("Ingrese un numero "))
nm5 = float(input("Ingrese un numero "))

promedio = ((nm1 + nm2 + nm3 + nm4 + nm5)/5)
print(promedio)

# Ejercicio #14

npares = int(input("Ingrese un numero "))

for i in range(1, npares + 1):
    if i % 2 == 0:
        print(i)

# Ejercicio #15

dletra = str(input("Ingrese una letra "))
vocales = ("a","e","i","o","u")

if dletra in vocales:
    print("Es una Vocal ")
else:
    print("No es un Vocal")

# Ejercicio #16

nfibo1 = 0
nfibo2 = 1

print(nfibo1, nfibo2, end=" ")

for i in range (2, 21):
    seriefibo = ((nfibo1 + nfibo2))
    print(seriefibo, end=" ")
    nfibo1 = nfibo2
    nfibo2 = seriefibo

# Ejercicio #17

nprimo = int(input("Ingrese un numero "))

if nprimo < 2:
    print("No es primo")
else:
    siprimo = True
    for i in range (2, nprimo):
        if nprimo % i == 0:
            siprimo = False
            break
    if siprimo:
        print("Si es primo")
    else:
        print("No es primo")

# Ejercicio #18

for i in range (1, 101):
    if i % 5 == 0:
        print(i)

# Ejercicio #19
npalabra = str(input("Ingrese una palabra "))
vocales1 = ("a","e","i","o","u")
nvocales = 0

for letra in npalabra:
    if letra in vocales1:
        nvocales += 1
print(nvocales)

# Ejercicio #20

opcion = ""

while opcion != "5":
    print("\n Calcular ")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        c = int(input("Ingrese el numero 1 "))
        d = int(input("ingrese el numero 2 "))
        sumar = c + d
        print(sumar)
    elif opcion == "2":
        c = int(input("Ingrese el numero 1 "))
        d = int(input("ingrese el numero 2 "))
        restar = c - d
        print(restar)
    elif opcion == "3":
        c = int(input("Ingrese el numero 1 "))
        d = int(input("ingrese el numero 2 "))
        multiplicar = c * d
        print(multiplicar)
    elif opcion == "4":
        c = int(input("Ingrese el numero 1 "))
        d = int(input("ingrese el numero 2 "))
        dividir = c / d
        print(dividir)
    elif opcion == "5":
        print("Saliendo del programa")
    else:
        print("Elija una Opcion valida")

# Ejercicio #21

lista1 = [12, 22, 21, 43, 54, 10, 21, 23, 43, 55]

nmayor = lista1[0]

for i in lista1:
    if i > nmayor:
        nmayor = i

print("La lista es: ", lista1)
print("El numero mayor en la lista es: ", nmayor)

# Ejercicio #22

lista2 = [12, 22, 21, 43, 54, 10, 21, 23, 43, 55]

n = len(lista2)
for i in range(n):
    for j in range(0, n - i - 1):
        if lista2[j] > lista2[j + 1]:
            lista2[j], lista2[j + 1] = lista2[j + 1], lista2[j]
print("Lista ordenada de menor a mayor es: ", lista2)

# Ejercicio #23

lista3 = [12, 22, 21, 43, 54, 10, 21, 23, 43, 55]

norepe = []

for i in lista3:
    if i not in norepe:
        norepe = norepe + [i]
print("La lista sin numeros repetidos es: ",norepe)

# Ejercicio #24

listanombre = ["camilo", "carlos", "luis", "david", "harold", "dilan", "ibis"]

n = len(listanombre)
for i in range(n):
    for j in range(0, n - i - 1):
        if listanombre[j] > listanombre[j + 1]:
            listanombre[j], listanombre[j + 1] = listanombre[j + 1], listanombre[j]
print("Lista ordenada de menor a mayor es: ", listanombre)

# Ejercicio #25

listasumar = [2, 2, 3, 4, 5, 7]
sumatt = 0
for i in listasumar:
    sumatt = sumatt + i
print("la lista es: ", listasumar)
print("La suma de esta lista es: ", sumatt)

# Ejercicio #26

lis1 = [1, 2, 3]
lis2 = [4, 5, 6]
lis3 = lis1 + lis2
print(lis3)

# Ejercicio #27

frase1 = str(input("Ingrese una frase "))
palabrastt = 1

for letra in frase1:
    if letra == " ":
        palabrastt += 1
print("El total de palabras es: ", palabrastt)

# Ejercicio #28

palabra = str(input("Ingresa una palabra "))    
alreves = palabra[::-1]

if alreves == palabra:
    print("Es un palindrome")
else:
    print("No es un palindrome")

# Ejercicio #29

cuadrados = []
for i in range(1, 11):
    cuadrados = cuadrados + [i*i]
print(cuadrados)

# Ejercicio #30

listax = [1, 2, 3, 4, 51, 52]
nummayor = listax[0]

for i in listax:
    if i > nummayor:
        nummayor = i

segundom = None
for i in listax:
    if i != nummayor:
        if segundom is None or i > segundom:
            segundom = i
print("la lista es: ", listax)
print("El segundo numero mayor es: ", segundom)
