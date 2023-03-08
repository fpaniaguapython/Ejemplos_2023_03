try:
    fichero = open("noexiste.txt","r")
    fichero.read()
    fichero.close()
except FileNotFoundError:
    print("Fichero no encontrado")

try:
    with open("noexiste.txt","r") as fichero:
        fichero.read()
except FileNotFoundError:
    print("Fichero no encontrado")