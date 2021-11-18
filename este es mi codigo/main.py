from Registro import Registro
from Matricula import Matricula
 
if __name__ == '__main__':
    run = True
    while(run):
        print("\n|REGISTRO DE ESTUDIENTES|\n")
        select = int(input("Seleccione la opcio que hara:\n1-Asignar Carrera\n2-Matricular estudiantes\n3-Revisar la matricula\n4-Salir\n:"))
        
        if select == 1:
            nombre = input("Dijite el nombre de la carrera: ")
            registro = Registro(nombre)
            print("\nSe asigno la carrera ~{}~ correctamente!".format(registro.Asisnar_carrera(nombre)))
            
        elif select == 2:
            nombre_y_apellido = input("Nombre y Apellido: ")
            edad = input("Edad: ")
            cedula = input("Numero de cedula: ")
            sexo = input("Sexo: ")
            estado_civil = input("Estado Civil: ")
            direccion = input("Direccion: ")
            numero_telefono = input("Numero de Celular: ")
            correo_electronico = input("Correo Electronico: ")
            
            matricula = Matricula(nombre_y_apellido , edad, cedula, sexo, estado_civil, direccion, numero_telefono, correo_electronico)
            registro.matricular_estudiante(matricula)
        elif select == 3:
            print("|MATRICULA ACTUAL|")
            for i in registro.ver_matricula():
                print(i)
        elif select == 4:
            run = False