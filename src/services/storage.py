"""Servicio de persistencia: guarda y carga el usuario en un archivo JSON."""

import json
from pathlib import Path

from src.models.usuario import Usuario


class StorageService:
    """Guarda y carga un Usuario desde un archivo JSON."""

    def guardar_usuario(self, usuario: Usuario, filepath: str) -> bool:
        """Guarda el usuario en un archivo JSON. Devuelve True si se pudo guardar."""
        try:
            Path(filepath).parent.mkdir(parents=True, exist_ok=True)
            with open(filepath, "w", encoding="utf-8") as archivo:
                json.dump(usuario.to_dict(), archivo, indent=4, ensure_ascii=False)
            return True
        except (OSError, TypeError):
            return False

    def cargar_usuario(self, filepath: str) -> Usuario:
        """Carga el usuario desde un archivo JSON.

        Returns:
            El usuario guardado, o `Usuario("Invitado", 0)` si el archivo no existe
            o sus datos no son válidos.
        """
        try:
            with open(filepath, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
            return Usuario.from_dict(datos)
        except (ValueError, OSError, json.JSONDecodeError, KeyError, TypeError):
            return Usuario("Invitado", 0)
