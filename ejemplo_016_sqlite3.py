import sqlite3

DB_NAME="./peliculas.db"

def create_squema():
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS peliculas " + 
                   "(id INTEGER PRIMARY KEY AUTOINCREMENT," + 
                   "titulo TEXT NOT NULL, " +
                   "director TEXT NOT NULL, " +
                   "anyo_estreno INTEGER NOT NULL)")
    connection.commit()
    cursor.close()

#CRUD
def create(titulo, director, anyo_estreno):
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO peliculas (titulo, director, anyo_estreno) " +
                   f"VALUES ('{titulo}','{director}',{anyo_estreno})")
    connection.commit()
    cursor.close()

#Devuelve tupla
def read(id):
    cursor = connection.cursor()
    pelicula = cursor.execute(f"SELECT * from peliculas WHERE ID={id}").fetchone()
    cursor.close()
    return pelicula

#Devuelve una lista de tuplas
def read_all():
    cursor = connection.cursor()
    peliculas = cursor.execute("SELECT * from peliculas").fetchall()
    cursor.close()
    return peliculas

def update(id, anyo):
    cursor = connection.cursor()
    cursor.execute("UPDATE peliculas SET anyo_estreno=? WHERE id=?",(anyo, id))
    connection.commit()
    cursor.close()

def delete(id):
    cursor = connection.cursor()
    cursor.execute("DELETE from peliculas WHERE id=?",(id,))
    connection.commit()
    cursor.close()

if __name__=="__main__":
    #APERTURA DE LA CONEXIÓN
    connection = sqlite3.connect(DB_NAME)
    #CREACIÓN DEL ESQUEMA DE LA BASE DE DATOS
    create_squema()

    
    
    #CREATE
    # titulo = input("Título:")
    # director = input("Director:")
    # anyo_estreno = int(input("Año de estreno:"))
    # create(titulo, director, anyo_estreno=anyo_estreno) 
    
    #READ_ALL
    # pelis = read_all()
    # for peli in pelis:
    #     print(f"ID:{peli[0]} Título:{peli[1]} Director:{peli[2]} Año:{peli[3]}")
    
    #READ_ONE
    # id = int(input("Identificador:"))
    # peli = read(id)
    # print(f"ID:{peli[0]} Título:{peli[1]} Director:{peli[2]} Año:{peli[3]}")
    
    #UPDATE
    #id = int(input("Introduce el identificador de la película a modificar:"))
    #anyo = int(input("Introduce el nuevo año:"))
    #update(id, anyo)

    #DELETE
    id = int(input("Introduce el identificador de la película a borrar:"))
    delete(id)

    #CIERRE DE LA CONEXIÓN
    connection.close()
    