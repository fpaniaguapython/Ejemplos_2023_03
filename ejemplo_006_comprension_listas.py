def traducir(palabra : str) -> str:
    diccionario = {"Perro":"Dog","Barco":"Ship","Casa":"House","Manzana":"Apple"}
    #return diccionario[palabra]#Si la palabra no existe -> KeyError
    return diccionario.get(palabra,"NO EXISTE")

    
lista = ["Perro","Barco","Gato","Casa","Manzana"]
#Con comprensión de listas, obtener una versión traducida de la lista de palabras
salida = [traducir(linea) for linea in lista]
print(salida)