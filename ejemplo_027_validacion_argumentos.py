"""
exception TypeError
Raised when an operation or function is applied to an object 
of inappropriate type. The associated value is a string giving 
details about the type mismatch.
This exception may be raised by user code to indicate that an
attempted operation on an object is not supported, and is not 
meant to be. If an object is meant to support a given operation 
but has not yet provided an implementation, NotImplementedError 
is the proper exception to raise.
Passing arguments of the wrong type (e.g. passing a list when an 
int is expected) should result in a TypeError, but passing arguments
with the wrong value (e.g. a number outside expected boundaries)
should result in a ValueError.
"""
def sumar(s1, s2):
    raise NotImplementedError("Función no implementada")

def restar(r1, r2):
    if not isinstance(r1, int) or not isinstance(r2, int):
        raise TypeError("Los argumentos deben ser enteros")
    return r1-r2

def dividir(d1, d2):
    if d2==0:
        raise ValueError("El divisor no puede ser 0")
    return d1/d2

#sumar(3,2) #Genera un error de tipo NotImplementedError
#restar("3",8) #Genera un error de tipo TypeError
#dividir(9,0) #Genera un erro de tipo ValueError

