from dataclasses import dataclass, field
from typing import Any

from src.models.habito import Habito


@dataclass
class Usuario:
    nombre: str
    edad: int
    rutina: list[Habito] = field(default_factory=list)

    def anadir_habito(self, habito: Habito) -> None:
        for existente in self.rutina:
            if existente.nombre.lower() == habito.nombre.lower():
                raise ValueError("Ya existe un habito con ese nombre en tu rutina")
        self.rutina.append(habito)

    def eliminar_habito(self, nombre: str) -> bool:
    da
        # TODO: Recorre la rutina, si encuentra habito, se quita con self.rutina.remove(habito) y devuelve True
         
        # TODO: si termina el for sin encontrarlo devuelve False
        pass

    def editar_habito(self, nombre: str) -> None:
        # TODO 1: Recorre la rutina, si encuentra habito, obtiene su json con to_dict
        # TODO  : lo modifica y luego lo devuelve con from_dict
        pass

    def obtener_porcentaje_global(self) -> float:
        """Calcula el progreso promedio de todos los hábitos (0 a 100)."""
        # TODO 1: si la rutina está vacía, devuelve 0.0 (evita dividir entre cero)
        # TODO 2: por cada hábito calcula su porcentaje:
        #         min(progreso_actual / meta_diaria, 1) * 100
        #         (min limita a 100 si te pasaste de la meta)
        # TODO 3: suma todos y divide entre la cantidad de hábitos
        pass

    def obtener_resumen_dia(self) -> dict[str, Any]:
        """Devuelve un resumen con totales del día."""
        # TODO: diccionario con las claves "total", "completados",
        #       "pendientes" y "porcentaje_global"
        pass

    def to_dict(self) -> dict[str, Any]:
        """Convierte el usuario (y su rutina) a un diccionario."""
        # TODO: "nombre", "edad" y "rutina": una lista por comprensión
        #       con h.to_dict() por cada hábito
        pass

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Usuario":
        """Crea un Usuario (y sus hábitos) desde un diccionario."""
        # TODO: reconstruye la rutina con Habito.from_dict por cada
        #       elemento de data.get("rutina", []), y devuelve cls(...)
        pass