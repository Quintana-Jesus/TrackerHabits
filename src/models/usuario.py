"""Modelo de dominio que representa un usuario con sus hábitos y rutina diaria."""

from dataclasses import dataclass, field
from typing import Any

from src.models.habito import Habito


@dataclass
class Usuario:
    """Representa un usuario con su rutina diaria."""
    nombre: str
    edad: int
    rutina: list[Habito] = field(default_factory=list)

    def anadir_habito(self, habito: Habito) -> None:
        """Añade un hábito a la rutina.

        Raises:
            ValueError: Si ya existe un hábito con ese nombre (sin importar mayúsculas).
        """
        for elemento_existente in self.rutina:
            if elemento_existente.nombre.lower() == habito.nombre.lower():
                raise ValueError("Ya existe un habito con ese nombre en tu rutina")
        self.rutina.append(habito)

    def eliminar_habito(self, nombre: str) -> bool:
        """Elimina un hábito por nombre. Devuelve True si existía y False si no."""
        for habito in self.rutina:
            if habito.nombre.lower() == nombre.lower():
                self.rutina.remove(habito)
                return True
        return False

    def obtener_porcentaje_global(self) -> float:
        """Calcula el porcentaje promedio de avance de todos los hábitos (0 a 100)."""
        if len(self.rutina) == 0:
            return 0.0
        total = 0.0
        for habito in self.rutina:
            porcentaje = min(habito.progreso_actual / habito.meta_diaria, 1) * 100
            total += porcentaje
        return total / len(self.rutina)

    def obtener_resumen_dia(self) -> dict[str, Any]:
        """Devuelve el total de hábitos, completados, pendientes y porcentaje global."""
        total = len(self.rutina)
        completados = 0
        pendientes = 0
        for habito in self.rutina:
            if habito.completado:
                completados += 1
            else:
                pendientes += 1
        porcentaje = self.obtener_porcentaje_global()
        return {
            "total": total,
            "completados": completados,
            "pendientes": pendientes,
            "porcentaje_global": porcentaje,
        }

    def to_dict(self) -> dict[str, Any]:
        """Convierte el usuario y su rutina en un diccionario listo para JSON."""
        return {
            "nombre": self.nombre,
            "edad": self.edad,
            "rutina": [h.to_dict() for h in self.rutina],
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Usuario":
        """Crea un usuario a partir de un diccionario. `rutina` es opcional.

        Raises:
            KeyError: Si falta `nombre` o `edad`.
            ValueError: Si algún hábito de la rutina tiene datos inválidos.
        """
        rutina = [Habito.from_dict(d) for d in data.get("rutina", [])]
        return cls(
            nombre=data["nombre"],
            edad=data["edad"],
            rutina=rutina,
        )
