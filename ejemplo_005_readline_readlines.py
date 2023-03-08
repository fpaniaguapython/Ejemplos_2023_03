with open("datos.txt",mode="r",encoding="utf-8") as fichero:
    #linea = fichero.readline()[:-1]#Eliminamos el último carácter, pero todas las líneas deben terminar en salto de línea
    while True:
        linea = fichero.readline().replace('\n','')
        """
        if linea=="": 
            print("FIN")
            break
        """
        if linea=="": print("FIN"); break
        print(linea)
  
with open("datos.txt",mode="r",encoding="utf-8") as fichero:
    lineas = fichero.readlines()
    print(lineas)

    #Opción 1
    lineas_limpias = list()
    for linea in lineas:
        linea=linea.replace('\n','')
        lineas_limpias.append(linea)
    print(lineas_limpias)

    #Opción 2
    lineas_copia = lineas[:]
    for i in range(0,len(lineas)):
        lineas_copia[i]=lineas_copia[i].replace('\n','')
    print(lineas_copia)
        
    #Opción 3
    lineas_limpias = [linea.replace('\n','') for linea in lineas]
    print(lineas_limpias)



