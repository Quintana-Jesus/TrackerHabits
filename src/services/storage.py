"""Servicio de persistencia: guarda y carga el usuario en un archivo JSON."""

import json
from pathlib import Path

from src.models.usuario import Usuario


class StorageService:
    """Guarda y carga un Usuario desde un archivo JSON."""

    def guardar_usuario(self, usuario: Usuario, filepath: str) -> bool:
        """Guarda el usuario en un archivo JSON.

        Returns:
            True si se guardó, False si ocurrió un error.
        """
        # TODO 1: try:
        #   - crea la carpeta con Path(filepath).parent.mkdir(...)
        #   - abre el archivo en modo "w" con encoding utf-8
        #   - json.dump(usuario.to_dict(), archivo, indent=4, ensure_ascii=False)
        #   - return True
        # TODO 2: except (OSError, TypeError): return False
        pass

    def cargar_usuario(self, filepath: str) -> Usuario:
        """Carga el usuario desde un archivo JSON.

        Si el archivo no existe o está corrupto, devuelve un usuario por defecto.
        """
        # TODO 1: try:
        #   - abre el archivo en modo "r" con encoding utf-8
        #   - datos = json.load(archivo)
        #   - return Usuario.from_dict(datos)
        # TODO 2: except (OSError, json.JSONDecodeError, KeyError, TypeError):
        #   - return un usuario por defecto, por ejemplo Usuario("Invitado", 0)
        pass