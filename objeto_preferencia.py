class AireC:

    def __init__(self):
        pass
    def Funcion(self):
        self._color()
        self._modelo()
        self._tamaño()
        self._precio()
        self._consumo_energetico()
        self._tipo_gas()
        self._calidad()
        self._categoria()

    def _color(self):
        print('descripcion de aire acondicionado\n')
        print('1.- El color es blanco\n')

    def _modelo(self):
        print('2.- El modelo es James\n')

    def _tamaño(slef):
        print('3.- El tamaño es: (ancho, alto, prof.) (802 x 285 x 195)\n')

    def _precio(self):
        print('4.- Su precio es de: USD430\n')

    def _consumo_energetico(self):
        print('5.- Consumo kWh: 1,208\n')

    def _tipo_gas(self):
        print('6.- El gas refrigerante es: R22\n')

    def _calidad(self):
        print('7.- muy beuna!\n')

    def _categoria(self):
        print('8.- sistema mono split')

if __name__=='__main__':
    aire_c=AireC()
    aire_c.Funcion()