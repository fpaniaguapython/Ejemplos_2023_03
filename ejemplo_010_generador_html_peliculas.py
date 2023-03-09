#Error Star Wars - Bug Miguel Ángel
def get_titulo_limpio(titulo):
    caracteres_prohibidos = ":?* "
    for caracter in caracteres_prohibidos:
        titulo = titulo.replace(caracter,'-')
    return titulo

def generar_documento_html_pelicula(titulo, poster, director):
    try:
        with open(get_titulo_limpio(titulo)+".html", "w", encoding="utf-8") as fichero:
            fichero.write("<html><head></head><body>")

            fichero.write(f"<h1>{titulo}</h1>")
            fichero.write(f"<h2>{director}</h2>")
            fichero.write(f"<img src='{poster}' width='200px'>")

            fichero.write("</body></html>")
            fichero.flush()
    except BaseException as e:
        print("Ha pasado algo malo:",e)