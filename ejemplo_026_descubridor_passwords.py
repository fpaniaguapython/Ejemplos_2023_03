import hashlib
import datetime

def get_hexdigest(pwd):
        m = hashlib.sha256()
        m.update(pwd.encode("utf-8"))#Convertimos la password a binario
        return m.hexdigest()

if __name__=="__main__":
    ms_inicial = datetime.datetime.now().microsecond

    fichero_hash = open("fernandopaniagua.txt","r")
    #fichero_hash = open("hash_prueba.txt","r")
    hash_almacenado = fichero_hash.read()
    fichero_hash.close()

    fichero = open("0_palabras_todas.txt","r",encoding="utf-8")
    #fichero = open("datos_prueba.txt","r",encoding="utf-8")
    contador=0
    for palabra in fichero:
        palabra = palabra.replace('\n','')
        hash_palabra = get_hexdigest(palabra)
        if hash_almacenado.upper()==hash_palabra.upper():
             print("EUREKA:",palabra)
             break
    fichero.close()
    ms_final = datetime.datetime.now().microsecond
    print(f"Hemos tardado {ms_final-ms_inicial} microsegundos")