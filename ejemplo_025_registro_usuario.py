import getpass
import hashlib

class Credencial:
    def __init__(self, id, pwd) -> None:
        self.id = id
        self.pwd = pwd

    def __repr__(self) -> str:
        pwd_cifrado = "*"*len(self.pwd)
        return f"Identificador:{self.id}. Password:{pwd_cifrado}"
    
    def get_hexdigest(self):
        m = hashlib.sha256()
        m.update(self.pwd.encode("utf-8"))#Convertimos la password a binario
        return m.hexdigest()

def get_credencial() -> Credencial:
    id = input("Introduce identificador de usuario:")
    pwd = getpass.getpass("Introduce contraseña:")
    credencial = Credencial(id, pwd)
    return credencial

def store_credencial(credencial : Credencial):
    hashpwd = credencial.get_hexdigest()
    nombre_fichero = f"{credencial.id}.txt"
    with open (nombre_fichero,"w") as fichero:
        fichero.write(hashpwd)

if __name__=="__main__":
    credencial = get_credencial()
    store_credencial(credencial)