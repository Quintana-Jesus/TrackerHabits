import pytest

from src.models.habito import Habito


def test_registrar_progreso_incrementa_el_progreso() -> None:
    habito = Habito("Beber agua", 8)
    resultado = habito.registrar_progreso(3)
    assert resultado is True
    assert habito.progreso_actual == 3


def test_completar_progreso() -> None:
    habito = Habito("Caminar", 8)
    habito.registrar_progreso(3)
    assert habito.completado is False
    habito.registrar_progreso(5)
    assert habito.completado is True


def test_registrar_progreso_invalido() -> None:
    habito = Habito("Correr", 8)
    resultado = habito.registrar_progreso(-2)
    assert resultado is False
    assert habito.progreso_actual == 0


def test_ida_y_vuelta() -> None:
    habito = Habito("Hacer ejercicio", 60)
    habito.registrar_progreso(45)
    datos = habito.to_dict()
    reconstruido = Habito.from_dict(datos)
    assert reconstruido == habito


def test_habito_con_meta_cero_lanza_error() -> None:
    with pytest.raises(ValueError):
        Habito("Estudiar", 0)


def test_habito_con_meta_negativa_lanza_error() -> None:
    with pytest.raises(ValueError):
        Habito("Tomar medicamento", -1)