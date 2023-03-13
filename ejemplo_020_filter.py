def es_par(numero):
    return numero%2==0

numeros = [3,8,10,1,4,15,20,21]

pares = filter(es_par, numeros) #Devuelve un objeto filter
print(list(pares))