#Ejercicio 1
def numeros_diccionario():
    numero = int(input("ingrese un numero entero positivo:"))

    if numero <= 0:
        print("Ingresa un numero entero positivo")
        return

    diccionario_numeros = {}
    for i in range (1, numero + 1 ):
        diccionario_numeros[i] = i ** 2
        
    print(diccionario_numeros)

numeros_diccionario()

#2 ejercicio phyton
def caracter(cadena):
  diccionario_caracteres={}
  for caracter in cadena:
    if caracter in diccionario_caracteres:
      diccionario_caracteres[caracter] +=1
    else:
      diccionario_caracteres[caracter] =1
  return diccionario_caracteres
 
cadena = input("ingrese una cadena: ")
resultado = caracter(cadena)
print("diccionario:", resultado)
print("apariciones:")
for caracter, cantidad in resultado.items():
  if caracter == ' ':
    print(f"espacios {cantidad} veces")
  else:
    print(f" '{caracter}'  {cantidad} veces")
caracter()
#Ejercicio 3

def programa_fruta():

    frutas = {
        "manzana": 2000,
        "banana": 1500,
        "pera": 3000,
        "naranja": 2500,
    }

    while True:
        fruta = input("Ingrese el nombre de la fruta que desea comprar (manzana, banana, pera, naranja): ").lower()
        try:
            cantidad = float(input("Ingrese la cantidad que se vendio: "))
        except ValueError:
            print("Cantidad inválida. Intente de nuevo.")
            continue

        if fruta in frutas:
            precio_total = frutas[fruta] * cantidad
            print(f"El precio total por {cantidad} de {fruta} es: {precio_total}")
        else:
            print("La fruta seleccionada no está disponible.")

        otra = input("¿Desea hacer otra compra? (si/no): ").lower()
        if otra not in ("si"):
            print("Gracias por su compra.")
            break


programa_fruta()
