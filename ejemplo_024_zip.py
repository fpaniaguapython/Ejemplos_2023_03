#EJEMPLO 'NORMAL'
temporada = ["Primavera","Verano","Otoño","Invierno"]
ingresos = [10_000, 15_000, 20_000, 1_500]
zip_ventas = zip(temporada, ingresos)#Devuelve un objeto de tipo zip
lista_ventas = list(zip_ventas)
for venta in lista_ventas:
    print(venta)

#EJEMPLO 'NORMAL' CON LISTAS DE DISTINTO TAMAÑO
temporada = ["Primavera","Verano","Otoño","Invierno","Entretiempo"]
ingresos = [10_000, 15_000, 20_000, 1_500]
zip_ventas = zip(temporada, ingresos)#Devuelve un objeto de tipo zip
lista_ventas = list(zip_ventas)
for venta in lista_ventas:
    print(venta)

#EJEMPLO 'NORMAL' CON LISTAS DE DISTINTO TAMAÑO
temporada = ["Primavera","Verano","Otoño","Invierno","Entretiempo"]
ingresos = [10_000, 15_000, 20_000, 1_500]
zip_ventas = zip(temporada, ingresos, strict=True)#Provoca un ValueError si los tamaños son distintos
lista_ventas = list(zip_ventas)
for venta in lista_ventas:
    print(venta)