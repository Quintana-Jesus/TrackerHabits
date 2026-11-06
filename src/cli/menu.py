from src.models.usuario import Usuario
from src.services.quote_service import QuoteService
from src.services.storage import StorageService


SEPARADOR = "=" * 40
ANCHO_BARRA = 16


def renderizar_barra(porcentaje: float) -> str:
    porcentaje = max(0, min(porcentaje, 100))
    llenos = int((porcentaje * ANCHO_BARRA) / 100)
    vacios = ANCHO_BARRA - llenos
    return f"[{"█"* llenos}{"░"*vacios}] {porcentaje:.1f}%"



def pedir_numero(mensaje: str) -> float:
    while True:
        texto = input(mensaje).strip()        
        try:
            numero = float(texto.replace(",", "."))
        except ValueError:
            print("Escribe un número válido.")
            continue
        if numero <= 0:
            print("Debe ser mayor que 0.")
            continue
        return numero


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
        # TODO: while True:
        #   - self._mostrar_menu()
        #   - opcion = input("Elige una opción: ").strip()
        #   - if opcion == "1": self._ver_resumen()
        #   - elif opcion == "6": print("¡Hasta luego!") y break
        #   - else: print("Opción no válida.")
        pass

    def _mostrar_menu(self) -> None:
        # TODO: imprime el SEPARADOR, el título y las 6 opciones
        pass

    def _ver_resumen(self) -> None:
        # TODO: ver los pasos abajo
        pass
