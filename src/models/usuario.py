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
        for habito in self.rutina:
            if habito.nombre.lower() == nombre.lower():
                self.rutina.remove(habito)
                return True
        return False

    def editar_habito(self, nombre: str) -> None:
        # TODO 1: Recorre la rutina, si encuentra habito, obtiene su json con to_dict
        # TODO  : lo modifica y luego lo devuelve con from_dict
        pass

    def obtener_porcentaje_global(self) -> float:
        if len(self.rutina) == 0:
            return 0.0
        total=0.0
        for habito in self.rutina:
            porcentaje = min(habito.progreso_actual / habito.meta_diaria, 1) * 100
            total += porcentaje
        return total / len(self.rutina)

    def obtener_resumen_dia(self) -> dict[str, Any]: 
        total = len(self.rutina)
        completados=0
        pendientes=0
        for habito in self.rutina:
            if habito.completado:
                completados += 1
            else:
                pendientes+=1
        porcentaje = self.obtener_porcentaje_global()
        return {
            "total": total,
            "completados": completados,
            "pendientes": pendientes,
            "porcentaje_global": porcentaje,
        }

    def to_dict(self) -> dict[str, Any]:
        return {
            "nombre": self.nombre,
            "edad": self.edad,
            "rutina": [h.to_dict() for h in self.rutina],
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Usuario":
        rutina = [Habito.from_dict(d) for d in data.get("rutina", [])]
        return cls(
            nombre=data["nombre"],
            edad=data["edad"],
            rutina=rutina, 
        )
    