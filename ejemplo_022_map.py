def mayuscular(palabra : str):
    return palabra.upper()

lista_palabras = ["ratón","impresora","pendrive"]

#Versión 'normal'
lista_tuneada = list(map(mayuscular, lista_palabras))

#Versión 'lambda'
#lista_tuneada = list(map(lambda w:w.upper(), lista_palabras))

print(lista_tuneada)