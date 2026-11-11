from src.cli.menu import Menu
from src.services.quote_service import QuoteService
from src.services.storage import StorageService

RUTA_DATOS = "data/rutina.json"


def main() -> None:
    storage = StorageService()
    quotes = QuoteService()
    usuario = storage.cargar_usuario(RUTA_DATOS)
    menu = Menu(usuario, storage, quotes, RUTA_DATOS)
    menu.ejecutar()


if __name__ == "__main__":
    main()
