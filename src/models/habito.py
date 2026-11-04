from dataclasses import dataclass
from typing import Any

@dataclass
class Habito:
    nombre: str
    meta_diaria: float
    progreso_actual: float = 0
    completado: bool = False
    categoria: str = "Salud" 

    def registrar_progreso(self, cantidad: float) -> bool:
        if cantidad <= 0:
            return False
        self.progreso_actual += cantidad
        if self.progreso_actual >= self.meta_diaria:
            self.completado=True
        return True

    def resetear_dia(self) -> None:
        self.progreso_actual = 0
        self.completado = False

    def to_dict(self) -> dict[str, Any]:
        return {
            "nombre": self.nombre,
            "meta_diaria": self.meta_diaria,
            "progreso_actual": self.progreso_actual,
            "completado": self.completado,
            "categoria": self.categoria,
        }

    @classmethod
    def from_dict(cls ,data:dict[str,Any]) -> "Habito":
        return cls(
            nombre=data["nombre"],
            meta_diaria=data["meta_diaria"],
            progreso_actual=data["progreso_actual"],
            completado=data["completado"],
            categoria=data["categoria"],
        )
