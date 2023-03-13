with open("codigo_para_eval.txt") as fichero:
    lineas_codigo = fichero.readlines()
    for linea_codigo in lineas_codigo:
        linea_limpia = linea_codigo.replace('\n','')
        eval(linea_limpia)