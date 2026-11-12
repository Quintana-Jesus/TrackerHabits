"""Modelo de dominio que representa un habito con su meta y progreso diario."""

from dataclasses import dataclass
from typing import Any


@dataclass
class Habito:
    """Representa un hábito con una meta diaria y su progreso actual.

    Attributes:
        nombre: Nombre del hábito.
        meta_diaria: Cantidad que se debe alcanzar cada día. Debe ser mayor que 0.
        progreso_actual: Cantidad acumulada en el día. Empieza en 0.
        completado: True si el progreso alcanzó la meta del día.
        categoria: Categoría del hábito. Por defecto es "Salud".
    """

    nombre: str
    meta_diaria: float
    progreso_actual: float = 0
    completado: bool = False
    categoria: str = "Salud"

    def __post_init__(self) -> None:
        """Valida que la meta diaria sea mayor que 0 al crear el hábito.

        Raises:
            ValueError: Si `meta_diaria` es menor o igual que 0.
        """
        if self.meta_diaria <= 0:
            raise ValueError("La meta diaria debe ser mayor que 0.")

    def registrar_progreso(self, cantidad: float) -> bool:
        """Suma una cantidad al progreso del día y marca el hábito si llega a la meta.

        Args:
            cantidad: Cantidad a sumar. Debe ser mayor que 0.

        Returns:
            True si se registró el progreso, False si la cantidad no es válida
            (menor o igual que 0) y no se cambió nada.
        """
        if cantidad <= 0:
            return False
        self.progreso_actual += cantidad
        if self.progreso_actual >= self.meta_diaria:
            self.completado = True
        return True

    def resetear_dia(self) -> None:
        """Reinicia el día: pone el progreso en 0 y `completado` en False."""
        self.progreso_actual = 0
        self.completado = False

    def to_dict(self) -> dict[str, Any]:
        """Convierte el hábito en un diccionario listo para guardarse en JSON.

        Returns:
            Diccionario con las claves `nombre`, `meta_diaria`, `progreso_actual`,
            `completado` y `categoria`.
        """
        return {
            "nombre": self.nombre,
            "meta_diaria": self.meta_diaria,
            "progreso_actual": self.progreso_actual,
            "completado": self.completado,
            "categoria": self.categoria,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Habito":
        """Crea un hábito a partir de un diccionario (por ejemplo, leído de JSON).

        Los campos `nombre` y `meta_diaria` son obligatorios. Los demás son
        opcionales:
            `progreso_actual` = 0,
            `completado` = False,
            `categoria` = "Salud",
            si no aparecen.

        Args:
            data: Diccionario con los datos del hábito.

        Returns:
            Un nuevo `Habito` con los datos del diccionario.

        Raises:
            KeyError: Si falta `nombre` o `meta_diaria`.
            ValueError: Si `meta_diaria` es menor o igual que 0.
        """
        return cls(
            nombre=data["nombre"],
            meta_diaria=data["meta_diaria"],
            progreso_actual=data.get("progreso_actual", 0),
            completado=data.get("completado", False),
            categoria=data.get("categoria", "Salud"),
        )
