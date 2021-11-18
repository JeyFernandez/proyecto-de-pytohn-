class ComprarPC:

    #creando mi clase para mi proograma
    def __init__(self):
        pass
        #mi init es un constructor incializo mi metodo
    def Comprar(self,Marca='Comprala'):
            self._juntar_el_dinero_para_la_compra(Marca)
            self._Ir_al_centro_comercial()
            self._fijar_el_equipo()
            self._Preguntar_acerca_de_la_marca()
            self._verificar_el_procesador_y_almacenamiento()
            self._revision_en_el_equipo()
            self._preguntar_la_garantia_del_equipo()
            self._negociar()
            self._Pensar_si_se_compra_o_no()
        #uso  el guion bajo para representar mi atributo privado
    def _juntar_el_dinero_para_la_compra(self, Marca):
        print(f'El dinero esta juntado {Marca}')

    def _Ir_al_centro_comercial(self):
        print('LLendo en la busqueda de la Pc')
    
    def _fijar_el_equipo(self):
        print('Pc encontrada')

    def _Preguntar_acerca_de_la_marca(self):
        print('preguntar el costo de la pc')

    def _verificar_el_procesador_y_almacenamiento(self):
        print('Revisar memoria Ram')

    def _revision_en_el_equipo(self):
        print('verificar la targeta grafica')

    def _preguntar_la_garantia_del_equipo(self):
        print('tiempo de garantia de la pc')
    
    def _negociar(self):
        print('Descuento aprobado en el equipo')

    def _Pensar_si_se_compra_o_no(self):
        print('la computadora esta comprada')

if __name__ == '__main__':
    comprar  = ComprarPC()
    comprar.Comprar()
