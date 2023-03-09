divisor = int(input("Divisor:"))
try:
    print("Línea 1")
    print("Línea 2")
    x = 8 / divisor
except:
    print("Error")
else:
    print("Línea 3")
finally:
    print("Siempre")
print("Línea 4")