class Circulos():
    #nombramiento de mi clase circulo
    def Dibujar(self):
    #defino un metodo llamado Dibujar
        print("1. Dibujando un circulo \n")

class Cuadrado():
    def Dibujar(self):
        print("2. Dibujando Cuadradado \n")

class Rectangulo():
    def Dibujar(self):
        print("3. Dibujando Rectangulo \n")

class Octagono():
    def Dibujar(self):
        print("4. Dibujando Octagono \n")

class Trinagulo():
    def Dibujar(self):
        print("5. Dibujando Trinagulo \n")
class Romboide():
    def Dibujar(self):
        print("6. Dibujado Romboide\n")

def Formas(dibujo):
    #defino un metodo llamado formas con un parametro llamado dibujo
    dibujo.Dibujar()
    #voy a instamciar mi parametro con el metodo dibujar
if __name__=='__main__':
    #para indocar a cmi compilador lo que deseo mostrar
    forma1 = Circulos()
    forma2 = Cuadrado()
    forma3 = Rectangulo()
    forma4 = Octagono()
    forma5 = Trinagulo()
    forma6 = Romboide()

    
    Formas(forma1)
    Formas(forma2)
    Formas(forma3)
    Formas(forma4)
    Formas(forma5)
    Formas(forma6)