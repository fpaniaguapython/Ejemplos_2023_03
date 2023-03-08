fichero = open("elquijote.txt",mode="r",encoding="utf-8")

primeros_19 = fichero.read(19)#Primeros 19 caracteres
diez = fichero.read(10)#Los siguientes 10 caracteres
fichero.seek(11)#Posicionamiento absoluto en el fichero
nombre_proyecto = fichero.read(8)#Leer los 8 siguientes caracteres a partir del posicionamiento
print(primeros_19)
print(diez)
print(nombre_proyecto)
fichero.close()