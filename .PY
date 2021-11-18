class Vehiculos():
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.freno=False

    def arranca(self):
        self.enmarcha=True

    def acelerar(self):
        self.acelera=True

    def frenar(self):
        self.freno=True
    
    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEnMarcha: ", self.enmarcha, 
            "\nAcelear: ", self.acelera, "\nFrenando: ", self.freno, "\n")

class Carro(Vehiculos):
    encuatroruedas=""
    def cuatroruedas(self):
        self.encuatroruedas="Vehiculo de cuatro ruedas"
    def estado1(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEnMarcha: ", self.enmarcha, 
            "\nAcelear: ", self.acelera, "\nFrenando: ", self.freno, "\nEnCuatroRuedas: ", self.encuatroruedas, "\n")

class Moto(Vehiculos):
    endosruedas=""
    def dosruedas(self):
        self.endosruedas="Vehiculo de dos ruedas"
    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEnMarcha: ", self.enmarcha, 
            "\nAcelear: ", self.acelera, "\nFrenando: ", self.freno, "\nEndosRuedas: ", self.endosruedas, "\n")

class Yate(Vehiculos):
    DeAgua=""
    Veloz=""
    def Acuatico(self):
        self.DeAgua="Vehiculo de agua"
        self.Veloz= "Es seguro y rapido"
    def estado2(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEnMarcha: ", self.enmarcha, 
            "\nAcelear: ", self.acelera, "\nFrenando: ", self.freno, "\nDeAgua: ", self.DeAgua, "\nVelocidad: ", self.Veloz, "\n")
          

MiMoto=Moto("Yamaha","XTZ")
MiMoto.dosruedas()
MiMoto.estado()

MiCarro=Carro("BMW","3.0 CSL.")
MiCarro.cuatroruedas()
MiCarro.estado1()

MiYate=Yate("Lürsen","Lürsen")
MiYate.Acuatico()
MiYate.estado2()


