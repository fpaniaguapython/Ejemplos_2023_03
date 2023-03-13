ciudades = [("Zaragoza",666000),("Albacete",173500),("Guadalajara",84910)]

def cuantificador_ciudades(ciudad):
    #Número de habitantes
    return ciudad[1]


print(sorted(ciudades, key=cuantificador_ciudades, reverse=True))