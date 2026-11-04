from schemas.habito import Habito

class Usuario:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        self.rutina = []

    def añadir_habito(self,objeto_habito,):
        self.rutina.append(objeto_habito)
        print(f"El habito {objeto_habito.nombre} fue asignado correctamente a {self.nombre}")

    def ver_progreso_del_dia(self):
        completados = 0
        print("===============================")
        print(f"          {self.nombre}   ")
        print("===============================")
        for habito in self.rutina:
            if habito.completado == True:
                completados+= 1
                print(f"[+] {habito.nombre} ({habito.progreso_actual}/{habito.meta_diaria})")
            else:
                print(f"[ ] {habito.nombre} ({habito.progreso_actual}/{habito.meta_diaria})")

        total_completados = len(self.rutina)
        if total_completados>0:
            porcentaje = (completados/total_completados)*100
        else:
            porcentaje = 0

        print(f"Progreso General de Hoy: {porcentaje:.2f}%")
        print("================================\n") 

    def actualizar_progreso_habito(self, nombre_buscar, cantidad):
        for habito in self.rutina:
            # Comparamos si el nombre coincide exactamente
            if habito.nombre == nombre_buscar:
                habito.registrar_progreso(cantidad)
                return  # Si lo encuentra, termina de buscar
        
        # Si termina el bucle for y no encontró el nombre
        print(f"No se encontró el hábito '{nombre_buscar}'")