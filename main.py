from schemas.habito import Habito
from schemas.usuario import Usuario

nombre_ingresado = input("Ingrese su nombre: ")
edad_ingresada = input("Digite su edad: ")

usuario1 = Usuario(nombre_ingresado,edad_ingresada)
ejecutando = True

while ejecutando:
    print("==================================")
    print("               MENU               ")
    print("==================================")
    print("1) Ver Progreso del Dia. ")
    print("2) Crear Nuevo Habito. ")
    print("3) Registrar Progreso en un Habito")
    print("4) Salir")
    print("----------------------------------")
    opcion = int(input("Seleccione Una Opción: "))

    while opcion<1 or opcion>4:
        print("ERROR! Opción Invalida")
        print("----------------------------------")
        opcion = int(input("Seleccione Una Opción Valida: "))

    match opcion:
        case 1:
            print("----- Ver Progreso del Dia -----")
            usuario1.ver_progreso_del_dia()

        case 2:
            print("----- Crear Nuevo Habito -----")
            nombre_habito = input("Nombre del Habito: ")
            meta_habito = int(input("Meta Diaria: "))

            nuevo_habito=Habito(nombre_habito,meta_habito)
            usuario1.añadir_habito(nuevo_habito)

        case 3:
            print("----- Registrar Progreso en un Habito -----")

            if len(usuario1.rutina)==0:
                print("No tienes Habitos Registrados")

            else:
                print(f"--- Habitos Registrados ---")
                for habitos in usuario1.rutina:
                    print(f"- {habitos.nombre}")
                print("===========================")

                nombre_habito=input("Ingrese el nombre del habito que desea ")
                cantidad_progreso = int(input("Digite el Progreso del Habito: "))

                usuario1.actualizar_progreso_habito(nombre_habito, cantidad_progreso)
