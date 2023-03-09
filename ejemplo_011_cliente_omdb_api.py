import requests
from ejemplo_010_generador_html_peliculas import generar_documento_html_pelicula as generador

API_KEY = "95c08eba"
URL = "https://www.omdbapi.com/"

def get_movie_info(url, api_key, titulo):
    #https://www.omdbapi.com/?apikey=95c08eba&t=Batman
    url_llamada = f"{url}/?apikey={api_key}&t={titulo}"
    respuesta = requests.get(url_llamada)
    if respuesta.status_code==200:
        movie_info = respuesta.json()
        return movie_info
    else:
        raise Exception("Ha ocurrido un error en la llamada:"+str(respuesta.status_code))

if __name__=="__main__":
    titulo = input("Introduce el título de la película:")
    try:
        movie_info = get_movie_info(URL, API_KEY, titulo)
        generador(movie_info.get("Title"),
                  movie_info.get("Poster"),
                  movie_info.get("Director"))
    except Exception as e:
        print(e)

