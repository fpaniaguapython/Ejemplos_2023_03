"""
1. Leer el fichero de elquijote.
2. Obtener una lista con todas las palabras
3. Convertir la lista a conjunto
4. Pedir al usuario una palabra e indicarle si existe o no.
EXTRA. No tenga en cuenta si las palabras están escritas en may. o min.
¿Qué hacemos con los caracteres 'extraños'?
"""
def leer_fichero(nombre_fichero):
    fichero = open(nombre_fichero, "r",encoding="utf-8")
    informacion = fichero.read()
    fichero.close()
    return informacion

def limpiar_texto(texto : str):
    simbolos_malos = ".,;()¿?¡!"
    for simbolo in simbolos_malos:
        texto = texto.replace(simbolo,"")
    return texto

def obtener_lista_palabras(texto):
    palabras = texto.split()
    return palabras

if __name__=="__main__":
    nombre_fichero = "elquijote.txt"
    texto = leer_fichero(nombre_fichero)
    texto = limpiar_texto(texto).upper()
    lista_palabras = obtener_lista_palabras(texto)
    conjunto_palabras = set(lista_palabras)

    palabra_a_buscar = input("Introduce una palabra:").upper()
    if palabra_a_buscar in conjunto_palabras:
        print("Existe")
    else:
        print("No existe")