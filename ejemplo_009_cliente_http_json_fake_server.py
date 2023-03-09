import requests
#import ejemplo_010_generador_html_peliculas
#import ejemplo_010_generador_html_peliculas as generador
#from ejemplo_010_generador_html_peliculas import generar_documento_html_pelicula
from ejemplo_010_generador_html_peliculas import generar_documento_html_pelicula as generador

URL = "https://fpaniaguapython.github.io/pelicula.json"

respuesta = requests.get(URL)
"""
print(respuesta.status_code)#200 OK
print(respuesta.ok)#True si status_code es <400
print(respuesta.text)
print(respuesta.json())
"""
if respuesta.status_code==200:
    pelicula = respuesta.json()
    generador(pelicula.get("Title"),pelicula.get("Poster"),pelicula.get("Director"))