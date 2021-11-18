class CompraPC:
    
    def __init__(self):
        pass
        
    def Compra(self, tarjeta='Tarjeta de credito'):
        self._revisar_presupuesto()
        self._ir_a_la_sucursal()
        self._buscar_caracteristica()
        self._ver_si_funciona()
        self._ir_a_caja()
        self._Pagar_con(tarjeta)
        self._armar_pc()
        self._difrutar_pc()    
       
    
    def _revisar_presupuesto(self):
        print('Su presupuesto alcanza para una gamin RAZEN 9 Xd\n')

    def _ir_a_la_sucursal(self):
        print('en este momento se enceuntra en la sucursal de computadoras\n')
    
    def _buscar_caracteristica(self):
        print('se estan buscado las caracteristica especificada')

    def _ver_si_funciona(self):
        print('su equipo esta en pruba\n')

    def _ir_a_caja(self):
        print('se esta cobrando la pc de su cuenta\n')

    def _Pagar_con(self,tarjeta):
        print(f'el pago se ha echo con {tarjeta} \n')
    
    def _armar_pc(self):
        print('su pc esta en proceso de ensamblaje\n')

    def _difrutar_pc(self):
        print('la pc esta lista para que la disfrute\n')
    


if __name__ == '__main__':
    compra_pc = CompraPC()
    compra_pc.Compra()