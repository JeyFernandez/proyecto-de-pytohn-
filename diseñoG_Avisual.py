class Desing:
    def __init__(self, programa, funcion):
        self.programa=programa
        self.funcion=funcion
    @property
    def NombreProgramas(self):
        return self.programa + '\n     ' + self.funcion
    @NombreProgramas.setter
    def NombreProgramas(self):
        self.programa, self.funcion

programa1=Desing('Adobe Photoshop:','Sirve para editar y crear imagenes')
programa2=Desing('Adobe Ilustrador:','sirve para elaborar representaciones visuales, o trasformaciones de la realidad')
programa3=Desing('Adobe XD:','sirve para crear prototipo de paginas web y app')
programa4=Desing('Adobe Lightroom:','es una app sencilla para trabajar imagenes dijitales')
programa5=Desing('Adobe Premier Pro:','es un editor de video con una amplia variedad de herramientas')
programa6=Desing('Adobe After Effects:','creacion de graficos profecionales en movimiento')

print(' ')
print(programa1.NombreProgramas,'\n',programa2.NombreProgramas,'\n',programa3.NombreProgramas)
print(programa4.NombreProgramas,'\n',programa5.NombreProgramas,'\n',programa6.NombreProgramas,'\n')