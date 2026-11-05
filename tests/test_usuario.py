import pytest

from src.models.habito import Habito
from src.models.usuario import Usuario


def test_anadir_habito_repetido_lanza_error():
    usuario = Usuario("Jesús", 20)
    usuario.anadir_habito(Habito("Correr", 30))

    with pytest.raises(ValueError):
        usuario.anadir_habito(Habito("correr", 10))


def test_eliminar_habito_existente_devuelve_true_y_lo_quita():
    usuario = Usuario("Jesús", 20)
    usuario.anadir_habito(Habito("Correr", 30))

    resultado = usuario.eliminar_habito("correr")

    assert resultado is True
    assert usuario.rutina == []


def test_eliminar_habito_inexistente_devuelve_false():
    usuario = Usuario("Jesús", 20)
    usuario.anadir_habito(Habito("Correr", 30))

    resultado = usuario.eliminar_habito("Nadar")

    assert resultado is False
    assert len(usuario.rutina) == 1


def test_porcentaje_global_con_rutina_vacia_es_cero():
    usuario = Usuario("Jesús", 20)

    assert usuario.obtener_porcentaje_global() == 0.0


def test_ida_y_vuelta_de_usuario():
    original = Usuario("Jesús", 20)
    agua = Habito("Beber agua", 8)
    agua.registrar_progreso(3)
    original.anadir_habito(agua)

    reconstruido = Usuario.from_dict(original.to_dict())

    assert reconstruido == original