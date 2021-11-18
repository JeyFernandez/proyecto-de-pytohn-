class ():
    def __init__(self, Creativo, ):
        self.creativo=Creativo

    def estado(self):
        print("Creatividad: ", self.creativo, "\nPensamiento: ", self.pensamiento, "\nResolutividad: ", self.resolutivo,"\n")

class ProgramadorJunior():
    Nombre=""
    edad =""
    
    def Junior(self):
        self.Nombre="Juan Carlos"
        self.edad="20"
    def estado(self):
        print("\nNombre: ",self.Nombre, "\nEdad: ", self.edad,  "\ncreatividad: ", self.creativo, "\nPensamiento: ", self.pensamiento, "\nResolutividad: ", self.resolutivo,  "\n")

programador_junior=ProgramadorJunior("Es creativo","bueno","Tiene potencial")
programador_junior.Junior()
programador_junior.estado()




