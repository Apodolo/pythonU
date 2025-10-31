# Ejercicio 1

frutas = ["manzana", "banano", "pera", "uva", "naranja"]

priemrelemento = frutas[0]
ultimoelemento = frutas[4]
print("Priemer y ultimo elemento: ", priemrelemento, " ", ultimoelemento)

frutas.append("mango")
print("Lista de frutas despues de agregar la fruta mango: ", frutas)

frutas.remove("pera")
print("lista actualizada: ", frutas)

# Ejercicio 2

numeros = [1,2,3,4,5,6,7,8,9,10]
total = sum(numeros)
print(total)

maximo = max(numeros)
print(maximo)

minimo = min(numeros)
print(minimo)

promedio = sum(numeros) / len(numeros)
print(promedio)

# Ejercicio 3
nombres = ["ana", "luis", "sofia", "carla", "pedro"]
print("todoslos nombres son")
for nombre in nombres:
  print(nombre)
 
print(" nombres con mas de cuatro letras")
for nombre in  nombres:
  if len(nombre)> 4:
    print(nombre)

#Ejercicio 4
edades = [12, 17, 18, 20, 15, 22, 13]
mayores = { edad for edad in  edades if edad >=18}
print("cantidad de persona mayores de edad:", len(mayores))
print("mayores de 18")
print(mayores)

# Ejercicio 5

notas = [3.5, 3.0, 5.0, 4.0]
promedionotas = sum(notas) / len(notas)
if promedionotas >= 3.0:
    print("aprobo")
else: "reprobo"

notasordenadas = sorted(notas)
print(notasordenadas)

# Ejercicio 6 

productos = []
precios = []

for i in range(5):
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    productos.append(nombre)
    precios.append(precio)

precio_total = sum(precios)
print("Precio total de todos los productos: ", precio_total)

producto_mas_caro = productos[precios.index(max(precios))]
producto_mas_barato = productos[precios.index(min(precios))]
print("Producto más caro: ", producto_mas_caro)
print("Producto más barato: ", producto_mas_barato)
