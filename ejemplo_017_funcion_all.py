def funcion1():
    return True

def funcion2():
    return True

def funcion3():
    return False

sensores = [funcion1(), funcion2(), funcion3()]
hay_peligro = all(sensores)
print("Hay peligro:",hay_peligro)