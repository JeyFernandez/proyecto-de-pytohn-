class Registro:
    def __init__(self, n_carrera):
        self.n_carrera = n_carrera
        self._n_estudiante = []

    def Asisnar_carrera(self, n_carrera):
        return self.n_carrera

    def matricular_estudiante(self, n_libro):
        self._n_estudiante.append({
            n_libro.nombre_y_apellido,
            n_libro.edad,
            n_libro.cedula,
            n_libro.sexo,
            n_libro.estado_civil,
            n_libro.direccion,
            n_libro.numero_telefono, 
            n_libro.correo_electronico
        }) 

    def ver_matricula(self):
        return self._n_estudiante