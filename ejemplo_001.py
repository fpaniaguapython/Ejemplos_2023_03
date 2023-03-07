def leer_fichero(nombre_fichero : str) -> str:
    fichero = open(nombre_fichero, "r")
    informacion = fichero.read()
    fichero.close()
    return informacion

if __name__=="__main__":
    contenido = leer_fichero("ejemplo_001.py")
    print(contenido.split())
