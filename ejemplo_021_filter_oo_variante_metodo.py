
class Factura:
    def __init__(self, id, importe) -> None:
        self.id = id
        self.importe = importe

    def __repr__(self) -> str:
        return str(self.id) + ":" + str(self.importe)
    
    def es_mayor(self):
        return self.importe > 1200

f1 = Factura(1, 1000)#Instanciación
f2 = Factura(2, 2000)
f3 = Factura(3, 1500)

facturas = [f1, f2, f3]
facturas_mayores = list(filter(Factura.es_mayor, facturas))
print(facturas_mayores)
