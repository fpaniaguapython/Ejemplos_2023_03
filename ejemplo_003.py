#w - Abre para escritura y trunca
fichero1 = open("fichero1.txt","w")
fichero1.write("CONTENIDO 2")
fichero1.close()

with open("fichero2.txt","w") as fichero2:
    fichero2.write("CONTENIDO DE FICHERO 2")

#x - Abre para escritura (falla si existe)
try:
    fichero3 = open("fichero3.txt","x")
    fichero3.close()
except FileExistsError:
    print("El fichero ya existe")

#a - Abre apra escritura y concatena
with open("fichero4.txt","a") as fichero4:
    fichero4.write("Lo que sea 2")