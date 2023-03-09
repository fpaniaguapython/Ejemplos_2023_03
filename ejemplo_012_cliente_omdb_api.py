import requests
from ejemplo_010_generador_html_peliculas import generar_documento_html_pelicula as generador

API_KEY = "95c08eba"
URL = "https://www.omdbapi.com/"

def get_movie_info(url, api_key, titulo):
    resultado ={"code":0,"data":None} #Objeto de retorno
    #https://www.omdbapi.com/?apikey=95c08eba&t=Batman
    url_llamada = f"{url}/?apikey={api_key}&t={titulo}"
    respuesta = requests.get(url_llamada)
    if respuesta.status_code==200:
        movie_info = respuesta.json()
        resultado["code"]=0
        resultado["data"]=movie_info
    else:
        resultado["code"]=-1
        resultado["data"]="Ha ocurrido un error"
    return resultado


if __name__=="__main__":
    titulo = input("Introduce el título de la película:")
    
    movie_info = get_movie_info(URL, API_KEY, titulo)
    if (movie_info["code"]==0):
        generador(movie_info["data"].get("Title"),
                    movie_info["data"].get("Poster"),
                    movie_info["data"].get("Director"))
    else:
        print("Ha ocurrido un erro:",movie_info["code"],movie_info["data"])
        
