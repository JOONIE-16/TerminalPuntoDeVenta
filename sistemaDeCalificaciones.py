# Algoritmo calificaciones

# Dimensionar arreglos
alumnos = [None] * 101
calificacion = [None] * 101

# Definir variables
total_alumnos = 0
opciones = 0

while opciones != 5:
    print("-----SISTEMA DE CALIFICACIONES-----")
    print("1. Registrar alumno")
    print("2. Mostrar alumnos")
    print("3. Editar alumno")
    print("4. Eliminar alumno")
    print("5. Salir del sistema")
    print("---SELECCIONE UNA OPCIÓN---")
    
    while True:
        try:
            opciones = int(input())
            break
        except ValueError:
            print("Error: Por favor, ingrese un número entero válido.")

    match opciones:
        case 1:
            if total_alumnos < 100:
                total_alumnos += 1
                print("Ingresa el nombre del alumno")
                alumnos[total_alumnos] = input()
                while True:
                    try:
                        print("Ingresa la calificacion")
                        calificacion[total_alumnos] = float(input())
                        break
                    except ValueError:
                        print("Error: Por favor, ingrese un número válido para la calificación.")
            else:
                print("Lista de alumnos completa")

        case 2:
            if total_alumnos == 0:
                print("NO HAY LISTA DE ALUMNOS")
            else:
                for i in range(1, total_alumnos + 1):
                    print("Alumno", i)
                    print("Nombre alumno", alumnos[i])
                    print("Calificación", calificacion[i])
                    print("------------------------")

        case 3:
            if total_alumnos == 0:
                print("NO HAY LISTA DE ALUMNOS")
            else:
                num_alumno_editar = 0
                while True:
                    try:
                        print("Ingrese el número del alumno a editar:")
                        num_alumno_editar = int(input())
                        break
                    except ValueError:
                        print("Error: Por favor, ingrese un número de alumno válido.")
                
                if 1 <= num_alumno_editar <= total_alumnos:
                    print("Ingresa el nuevo nombre del alumno")
                    alumnos[num_alumno_editar] = input()
                    while True:
                        try:
                            print("Ingresa la nueva calificacion")
                            calificacion[num_alumno_editar] = float(input())
                            break
                        except ValueError:
                            print("Error: Por favor, ingrese un número válido para la calificación.")
                    print("Alumno editado con éxito.")
                else:
                    print("Número de alumno no válido.")

        case 4:
            if total_alumnos == 0:
                print("NO HAY LISTA DE ALUMNOS")
            else:
                num_alumno_eliminar = 0
                while True:
                    try:
                        print("Ingrese el número del alumno a eliminar:")
                        num_alumno_eliminar = int(input())
                        break
                    except ValueError:
                        print("Error: Por favor, ingrese un número de alumno válido.")

                if 1 <= num_alumno_eliminar <= total_alumnos:
                    for i in range(num_alumno_eliminar, total_alumnos):
                        alumnos[i] = alumnos[i+1]
                        calificacion[i] = calificacion[i+1]
                    total_alumnos -= 1
                    print("Alumno eliminado con éxito.")
                else:
                    print("Número de alumno no válido.")

        case 5:
            print("Saliendo del sistema...")

        case _:
            print("Opción no válida")