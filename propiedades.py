class Alumno:
    def __init__(self, nombre, nombre2, apellido, apellido2):

        self.nombre=nombre
        self.nombre2=nombre2
        self.apellido=apellido
        
        self.apellido2=apellido2
    @property

    def nombreLista(self):
        return self.nombre +' ' + self.nombre2 + ' ' + self.apellido +' '+ self.apellido2
            
    @nombreLista.setter

    def nombreLista(self, NombreCompleto):
        self.nombre, self.apellido, self.apellido2, self.nombre = NombreCompleto

Alumno1 = Alumno('Jasson','Ariel', 'Fernandez', 'Espinoza')
Alumno2 = Alumno('Teresa','De Jesus', 'Morales', 'Ramirez')
Alumno3 = Alumno('Elliam','Elliam','Sanchez', 'Sanchez')

print(Alumno1.nombreLista)
print(Alumno2.nombreLista)
print(Alumno3.nombreLista)