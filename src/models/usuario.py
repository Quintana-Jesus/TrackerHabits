from dataclasses import dataclass, field
from typing import Any

from src.models.habito import Habito

@dataclass
class Usuario:
    nombre: str
    edad: int
    rutina: list[Habito] = field(default_factory=list)


    def anadir_habito(self, habito: Habito) -> None:
        # TODO 1: Recorre self.rutina si algun h.nombre es igual (sin importar mayuscula), lanza ValueError con un mensaje
        # TODO 2: Si no hay repetido, agrega con self.rutina.append(habito)
        pass

    def eliminar_habito(self, nombre: str) -> bool:
        # TODO: Recorre la rutina, si encuentra habito, se quita con self.rutina.remove(habito) y devuelve True
        # TODO: si termina el for sin encontrarlo devuelve False
        pass

    def editar_habito(self, nombre: str) -> None:
        # TODO 1: Recorre la rutina, si encuentra habito, obtiene su json con to_dict
        # TODO  : modifica y luego lo devuelve con from_dict
        pass