import json

def mostrar_a_lo_random(serie):
    #for k in serie.keys():
    #    print(k)
    
    #for v in serie.values():
    #    print(v)

    for k,v in serie.items():
        if (not isinstance(v,list)):
            print(k,":",v)
        else:
            for elemento in v:
                for k2, v2 in elemento.items():
                    print(k2,":",v2)
        #print(k,":",v)


def mostrar_ordenadamente(serie):
    print(f"Título:{serie['titulo']}")
    print(f"Director:{serie['director']}")
    print(f"Temporadas:{serie['numero_temporadas']}")
    for actor in serie['actores']:
        print(f"Nombre:{actor['nombre']}. Nacionalidad:{actor['nacionalidad']}")


fichero = open("datos.json",encoding="utf-8")
serie = json.load(fichero)
fichero.close()
mostrar_ordenadamente(serie)


