class Programas:
    def __init__(self, nombre, creacion, diseñador):

        self.nombre=nombre
        self.creacion=creacion
        self.diseñador=diseñador

    @property

    def nombreLenguajes(self):

        return self.nombre + '\n ' + self.creacion +'\n '+ self.diseñador
            
    @nombreLenguajes.setter
    def nombreLenguajes(self):
        self.nombre, self.creacion, self.diseñador

lenguaje1 = Programas('C#','se creo en: 2000','su diseñador: Microsoft')

lenguaje2 = Programas('Python', 'se creo en: 1991', 'su diseñador Guido van Rossum')

lenguaje3= Programas('C++','se creo en:  1980', 'su diseñador: Bjarne Stroustrup')

lenguaje4= Programas('Kotlin', 'se creo en:  2016', 'su diseñador: JetBrains')
    
lenguaje5= Programas('JavaScript','se creo en:  1995', 'su diseñador: Netscape Communications, Fundación Mozilla')

lenguaje6 =Programas('PHP' ,'se creo en:  1995', 'su diseñador: Rasmus Lerdorf')



print(lenguaje1.nombreLenguajes,'\n','\n',lenguaje2.nombreLenguajes,'\n','\n',lenguaje3.nombreLenguajes,'\n')
print(lenguaje4.nombreLenguajes,'\n','\n',lenguaje5.nombreLenguajes,'\n','\n',lenguaje6.nombreLenguajes,'\n')