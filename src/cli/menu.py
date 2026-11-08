from src.models.usuario import Usuario
from src.models.habito import Habito
from src.services.quote_service import QuoteService
from src.services.storage import StorageService


SEPARADOR = "=" * 40
ANCHO_BARRA = 16


def renderizar_barra(porcentaje: float) -> str:
    porcentaje = max(0, min(porcentaje, 100))
    llenos = int((porcentaje * ANCHO_BARRA) / 100)
    vacios = ANCHO_BARRA - llenos
    return f"[{'█'* llenos}{'░'*vacios}] {porcentaje:.1f}%"

def pedir_numero(mensaje: str) -> float:
    while True:
        texto = input(mensaje).strip()
        try:
            numero = float(texto.replace(",", "."))
        except ValueError:
            print("Escribe un numero válido.")
            continue
        if numero <= 0:
            print("Debe ser mayor que 0.")
            continue
        return numero

def pedir_texto(mensaje: str) -> str:
    while True:
        texto = input(mensaje).strip()
        if len(texto) == 0:
            print("El mensaje esta vacio.")
            continue
        return texto


class Menu:
    def __init__(
            self,
            usuario: Usuario,
            storage: StorageService,
            quotes: QuoteService,
            filepath: str,
        ) -> None:
        self.usuario = usuario
        self.storage = storage
        self.quotes = quotes
        self.filepath = filepath

    def ejecutar(self) -> None:
        while True:
            self._mostrar_menu()
            opcion = input("Elige una opcion: ").strip()
            if opcion == "1":
                self._ver_resumen()
            elif opcion == "2":
                self._registrar_progreso()
            elif opcion == "3":
                self._crear_habito()
            elif opcion == "4":
                self._eliminar_habito()
            elif opcion == "5":
                self._mostrar_frase()
            elif opcion == "6":
                print("Hasta luego!")
                break
            else:
                print("Opcion no valida.")

    def _mostrar_menu(self) -> None:
        print(SEPARADOR)
        print("\n  Tracker Habitos y Bienestar  \n")
        print(SEPARADOR)
        print(" 1. Ver resumen del dia")
        print(" 2. Registrar progreso en un hábito")
        print(" 3. Crear nuevo hábito")
        print(" 4. Eliminar hábito")
        print(" 5. Frase motivacional del dia")
        print(" 6. Guardar y salir")
        print(SEPARADOR)

    def _ver_resumen(self) -> None:
        resumen = self.usuario.obtener_resumen_dia()
        print(SEPARADOR)
        print(f"Resumen de {self.usuario.nombre}")
        print(
            f"Habitos: {resumen['total']} | "
            f"Completados: {resumen['completados']} | "
            f"Pendientes: {resumen['pendientes']}"
        )
        print(renderizar_barra(resumen["porcentaje_global"]))
        for habito in self.usuario.rutina:
            print(f"- {habito.nombre}: {habito.progreso_actual}/{habito.meta_diaria}")
        print(SEPARADOR)

    def _registrar_progreso(self) -> None:
        if len(self.usuario.rutina) == 0:
            print("No hay habitos registrados. Crea uno primero.")
            return
        nombre = input("Ingrese el nombre del habito: ").strip()
        habito_encontrado = None
        for habito in self.usuario.rutina:
            if habito.nombre.lower() == nombre.lower():
                habito_encontrado = habito
                break
        if habito_encontrado is None:
            print(f"{nombre} no se encuentra en tu rutina.")
            return
        
        cantidad = pedir_numero("Digite la cantidad del progreso: ")
        registrado = habito_encontrado.registrar_progreso(cantidad)
        if not registrado:
            print("No se pudo registrar el progreso.")
            return
        print(
            f"{habito_encontrado.nombre}: "
            f"{habito_encontrado.progreso_actual}/{habito_encontrado.meta_diaria}"
        )
        if habito_encontrado.completado:
            print("Felicidades! Completaste tu meta de hoy.")
        else:
            print("Genial! Estas mas cerca de completar tu hábito.")

    def _crear_habito(self) -> None:
        nombre = pedir_texto("Ingrese el nombre del habito: ")
        meta = pedir_numero("Digite su meta: ")
        habito = Habito(nombre, meta)
        try:
            self.usuario.anadir_habito(habito)
        except ValueError as error:
            print(error)
            return 
        print(f"Habito: {habito.nombre} ha sido creado. Meta: {habito.meta_diaria}")

    def _eliminar_habito(self) -> None:
        if len(self.usuario.rutina) == 0:
            print("No hay habitos registrados. Crea uno primero.")
            return 
        nombre = pedir_texto("Ingrese el nombre del habito que desea eliminar: ")
        eliminado = self.usuario.eliminar_habito(nombre)
        if eliminado:
            print(f"{nombre} ha sido eliminado correctamente.")
        else:
            print(f"{nombre} no existe en tu lista.")

    def _mostrar_frase(self) -> None:
        frase = self.quotes.obtener_frase()
        print(SEPARADOR)
        print(frase)
        print(SEPARADOR)