class Lavadora:
    #creamos la clase para mi programa
    def __init__(self):
        pass
        #mi init es un contructor, inicializo mi metodo
    def lavar(self, temperatura='caliente'):
            self._agregar_agua_al_tanque(temperatura)
            self._agregar_jabon()
            self._lavar_la_ropa()
            self._centrifugar()
        #uso el guion bajo para reprecentar mis atributos privados
    
    def _agregar_agua_al_tanque(self, temperatura):
        print(f'Llenando el tanque con agua {temperatura}')

    def _agregar_jabon(self):
        print('agregando el jabon o detergente liquido')

    def _lavar_la_ropa(self):
        print('Lavando la ropa')

    def _centrifugar(self):
        print('haciendo el proceso de secado de mi ropita')

if __name__ == '__main__':
    lavadora = Lavadora()
    lavadora.lavar()
