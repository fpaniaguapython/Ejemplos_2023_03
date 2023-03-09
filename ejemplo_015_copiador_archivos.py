#Pedir al usuario un nombre de fichero
#Copiar el fichero en varias ubicaciones
ubicaciones = ("//192.168.5.2/Users/CTA/OneDrive/Escritorio/Fila 1 PM",
               "//192.168.5.6/Users/CTA/Desktop/Fila 2 PM",
               "//192.168.5.10/Users/CTA/OneDrive/Escritorio/Fila 3 PM",
               "//192.168.5.14/Users/CTA/Desktop/Fila 4 PM")

nombre_fichero = input("Introduce el nombre del fichero:")
f_entrada= open(nombre_fichero,"rb")
fds = []#Lista de descriptores de fichero
for ubicacion in ubicaciones:
    fd = open(f"{ubicacion}/{nombre_fichero}","wb")
    fds.append(fd)

caracter = f_entrada.read(1)
while caracter:
    for fd in fds:
        fd.write(caracter)
    caracter = f_entrada.read(1)

for fd in fds:
    fd.close()