class IngenieroEnSistemas():

    def __init__(self, ApProgramacion, ApDesarrolloW,ApDesarrolloMovil):
        self.programacion=ApProgramacion
        self.desarrolloWeb=ApDesarrolloW
        self.desarrollomovil=ApDesarrolloMovil

    def estado(self):
        print("Aprendiendo: ", self.programacion, "\nAprendiendo: ", self.desarrolloWeb, 
        "\nAprendiendo: ", self.desarrollomovil, "\n")

class SegundoAño(IngenieroEnSistemas):
    skils =""
    def Segundo(self):
        self.skils="Python y C#"
    def pEstado(self):
        print("Desarrollo en: ",self.skils,"\nAprendiendo: ", self.programacion, 
        "\nAprendiendo: ", self.desarrolloWeb, "\nAprendiendo: ", self.desarrollomovil, "\n")

class TercerAño(IngenieroEnSistemas):
    skils1=""
    def Tercero(self):
        self.skils1="PHP y Python"
    def sEstado(self):
        print("Desarrollo en: ",self.skils1,"\nAprendiendo: ", self.programacion, 
        "\nAprendiendo: ", self.desarrolloWeb, "\nAprendiendo: ", self.desarrollomovil, "\n")

class CuartoAño(IngenieroEnSistemas):
    skils2=""
    def Cuarto(self):
        self.skils2="Kotlin y Swift"
    def tEstado(self):
        print("Desarrollo en:", self.skils2,"\nAprendiendo: ", self.programacion,
        "\nAprendiendo: ", self.desarrolloWeb, "\nAprendiendo: ", self.desarrolloWeb, "\n")

print("Segundo Año")
segundo=SegundoAño("Es muy bueno","Regular","Soso")
segundo.Segundo()
segundo.pEstado()

print("Tercer Año")
tercero=TercerAño("--","--","--")
tercero.Tercero()
tercero.sEstado()

print("Cuarto Año")
cuarto=CuartoAño("--","--","--")
cuarto.Cuarto()
cuarto.tEstado()
#Jasson Fernandez
#Teresa Morales