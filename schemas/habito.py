class Habito:
    def __init__(self,nombre,meta_diaria):
        self.nombre = nombre
        self.meta_diaria = meta_diaria
        self.progreso_actual = 0
        self.completado = False

    def registrar_progreso(self,cantidad):
        self.progreso_actual+=cantidad
        print(f"Sumaste {cantidad} a {self.nombre}. Progreso: {self.progreso_actual}/{self.meta_diaria}")
        if self.progreso_actual>=self.meta_diaria:
            self.completado = True
            print(f"¡Habito {self.nombre} completado por hoy!")