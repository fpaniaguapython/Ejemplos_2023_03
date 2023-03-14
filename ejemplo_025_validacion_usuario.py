import ejemplo_025_registro_usuario as registro


def get_hash_from_id(credencial_nueva):
    nombre_fichero = credencial_nueva.id + ".txt"
    with open(nombre_fichero, "r") as fichero:
        hash_almacenado = fichero.read()
    return hash_almacenado


if __name__=='__main__':
    credencial_nueva = registro.get_credencial()
    hash_nuevo = credencial_nueva.get_hexdigest()
    hash_almacenado = get_hash_from_id(credencial_nueva)
    print(hash_nuevo)
    print(hash_almacenado)
    if (hash_nuevo==hash_almacenado):
        print("OK")
    else:
        print("ERES UN IMPOSTOR")
