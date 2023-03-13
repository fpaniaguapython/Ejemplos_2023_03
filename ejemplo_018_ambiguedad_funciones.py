import math #math tiene una función cos(x)

def cos(x):
    return("Mi coseno local")

if __name__=="__main__":
    print(cos(5))#Ejecuta el de ámbito local
    print(math.cos(5))#Ejecuta el del módulo concreto

