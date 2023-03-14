import datetime

hoy = datetime.date.today() #Obtenemos un objeto DATE con la fecha actual
print(hoy.year)#Este año
print(hoy.month)#Este mes 
print(hoy.day)#Este día

ahora = datetime.datetime.now() #Obtenemos un objeto DATETIME con la hora actual
print(ahora.year)#Año
print(ahora.month)#Mes
print(ahora.day)#Día
print(ahora.hour)#Hora
print(ahora.minute)#Minuto
print(ahora.second)#Segundo
print(ahora.microsecond)#Microsegundo

#Calcular dentro de 10 días
diferencia = datetime.timedelta(days=10)#offset, desplazamiento en el tiempo
dentro_de_10_dias = hoy+diferencia
print(dentro_de_10_dias.day,"de",dentro_de_10_dias.month)

#Calcular dentro de 10 días y 4 horas
diferencia = datetime.timedelta(days=10, hours=4)#offset, desplazamiento en el tiempo
dentro_de_10_dias_y_4_horas = ahora+diferencia
print(dentro_de_10_dias_y_4_horas.day,"de",dentro_de_10_dias_y_4_horas.month)

#Calcular hace 4 días
diferencia = datetime.timedelta(days=4)#offset, desplazamiento en el tiempo
hace_4_dias = hoy-diferencia
print(hace_4_dias.day,"de",hace_4_dias.month)

nacimiento = datetime.date(1971,9,3)
hoy = datetime.date.today()
diferencia = hoy - nacimiento
print(diferencia.days)#Número de días entre dos fechas