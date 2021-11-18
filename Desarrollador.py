class Desarrolladores():
    #Mi clase principal
    def __init__(self, Creativo, PensamientoLogico,Resolutivo):
        self.creativo=Creativo
        self.pensamiento=PensamientoLogico
        self.resolutivo=Resolutivo
        #aca defino mis paramatros 
    def estado(self):
        print("Creatividad: ", self.creativo, "\nPensamiento: ", self.pensamiento, "\nResolutividad: ", self.resolutivo, "\n")

class ProgramadorJunior(Desarrolladores):
    skils =""
    def Junior(self):
        self.skils="C# y C++"
    def estado1(self):
        print("Skils: ",self.skils,"\nCreatividad: ", self.creativo, "\nPensamiento: ", self.pensamiento, "\nResolutividad: ", self.resolutivo, "\n")

class ProgramadorSemiSenior(Desarrolladores):
    skils1=""
    def SemiSenior(self):
        self.skils1="Kotlin y Swift"
    def estado2(self):
        print("Skils: ",self.skils1,"\nCreatividad: ", self.creativo, "\nPensamiento: ", self.pensamiento, "\nResolutividad: ", self.resolutivo, "\n")

class ProgramadorSenior(Desarrolladores):
    skils2=""
    def Senior(self):
        self.skils2="Python y PHP"
    def estado3(self):
        print("Sliks:", self.skils2,"\nCreatividad: ", self.creativo, "\nPensamiento: ", self.pensamiento, "\nResolutividad: ", self.resolutivo, "\n")
#creo subclases y agrego nuevas instancias        

print("ProgramadorJunior")
junior=ProgramadorJunior("Buena","Intermedio","Regular")
junior.Junior()
junior.estado1()

print("ProgramadorSemiSenior")
semisinior=ProgramadorSemiSenior("Regular","Muy Buena","Regular")
semisinior.SemiSenior()
semisinior.estado2()

print("ProgramadorSenior")
senior=ProgramadorSenior("Muy buena","Exelente","Buena")
senior.Senior()
senior.estado3()
#Jasson Fernandez
#Teresa Morales