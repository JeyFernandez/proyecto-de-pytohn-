class Cafetera:
    #creo la clase de el programa
    def __init__(self):
        pass
        #el init es un conductor he inicializo el programa
    def preparacion(self, temperatura=' temperatura ambiente', tipo='negro'):
        self._encendiendo_equipo()
        self._agregando_agua_al_recipiente(temperatura)
        self._agragando_cafe(tipo)
        self._proceso_de_ebullicion()
        self._filtrando_cafe_al_recipiente()
        self._sirviendo_cafe()
        self._agregando_azucar()
        self._tomar_cafe()    
        #uso el guion bajo para reprecentar los atributos privados
    
    def _encendiendo_equipo(self):
        print('1 se esta encendiendo su equipo\n')

    def _agregando_agua_al_recipiente(self, temperatura):
        print(f'2 se esta llenado el recipiente con agua {temperatura}\n')

    def _agragando_cafe(self,tipo):
        print(f'3 agragando cafe {tipo} al recipiente\n')

    def _proceso_de_ebullicion(self):
        print('4 el cafe esta en proceso\n')

    def _filtrando_cafe_al_recipiente(self):
        print('5 el cafe se esta filtrando\n')
    
    def _sirviendo_cafe(self):
        print('6 el cafe se esta sirviando en una taza\n')

    def _agregando_azucar(self):
        print('7 su cafe se esta endulzando\n')
    
    def _tomar_cafe(self):
        print('8 su cafe esta listo para tomar :) \n') 


if __name__ == '__main__':
    cafetera = Cafetera()
    cafetera.preparacion()