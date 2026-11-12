# PulseHabits CLI

Aplicación de consola en Python para llevar el seguimiento de hábitos de bienestar: defines tus hábitos con una meta diaria, registras tu progreso y ves tu avance en una barra de progreso. Está construida con una arquitectura en capas (modelos, servicios y CLI) y funciona sin conexión a internet.

## Qué hace

- **Ver resumen del día:** hábitos totales, completados y pendientes, con una barra de progreso global.
- **Registrar progreso:** suma una cantidad a un hábito y avisa cuando alcanzas la meta.
- **Crear y eliminar hábitos:** sin distinguir mayúsculas y sin permitir nombres repetidos.
- **Frase motivacional:** consulta la API pública de [ZenQuotes](https://zenquotes.io); si no hay internet, muestra una frase local.
- **Guardado automático:** los datos se guardan en un archivo JSON al salir, incluso si interrumpes el programa con `Ctrl+C`.

## Tecnologías

- Python 3.9 o superior (desarrollado y probado con Python 3.13)
- [requests](https://pypi.org/project/requests/) para consumir la API
- [pytest](https://pytest.org) para las pruebas
- [ruff](https://docs.astral.sh/ruff/) para revisar el estilo y dar formato al código
- Git y GitHub para el control de versiones

## Instalación y ejecución

Ejecuta todos los comandos desde la raíz del proyecto.

```bash
git clone https://github.com/Quintana-Jesus/TrackerHabits.git
cd TrackerHabits
python -m venv venv
```

Activa el entorno virtual:

```bash
# Windows (PowerShell)
venv\Scripts\Activate.ps1

# macOS / Linux
source venv/bin/activate
```

Instala las dependencias y ejecuta la app:

```bash
python -m pip install -r requirements.txt
python main.py
```

## Pruebas y calidad del código

Para correr las pruebas:

```bash
python -m pytest
```

Para revisar el estilo, los errores, los imports y los docstrings, y comprobar el formato (`ruff` no está en `requirements.txt`, se instala aparte):

```bash
python -m pip install ruff
ruff check .
ruff format --check .
```

## Estructura del proyecto

```
TrackerHabits/
├── data/                  # rutina.json (se genera al guardar, no se sube al repo)
├── src/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── habito.py      # entidad Habito
│   │   └── usuario.py     # entidad Usuario y su rutina
│   ├── services/
│   │   ├── __init__.py
│   │   ├── storage.py     # lectura y escritura del JSON
│   │   └── quote_service.py  # frase motivacional (API con respaldo local)
│   └── cli/
│       ├── __init__.py
│       └── menu.py        # menú interactivo en consola
├── tests/
│   ├── __init__.py
│   ├── test_habito.py
│   └── test_usuario.py
├── .gitignore
├── main.py                # punto de entrada
├── pyproject.toml         # configuración de ruff
├── requirements.txt
└── README.md
```

## Arquitectura en capas

El código está dividido en tres capas para que cada una tenga una sola responsabilidad:

- **Modelos (`src/models`):** contienen las reglas y el estado (`Habito`, `Usuario`) y saben convertirse a y desde diccionarios. No usan `print()` ni `input()`: así se pueden probar y reutilizar sin depender de la consola.
- **Servicios (`src/services`):** hablan con el exterior, es decir, el archivo JSON y la API de frases.
- **CLI (`src/cli`):** es lo único que muestra texto y pide datos al usuario.

`main.py` no tiene lógica: crea las piezas y se las pasa al menú, que las recibe en vez de crearlas él mismo (inyección de dependencias).

## Decisiones de diseño

- **La meta debe ser mayor que 0.** `Habito` lo valida al crearse (`__post_init__`) y lanza `ValueError`. Además evita una división entre cero al calcular el porcentaje.
- **Un JSON dañado no rompe la app.** Si el archivo no existe, está corrupto o trae datos inválidos, `cargar_usuario` devuelve un usuario `Invitado` en lugar de lanzar un error.
- **`Ctrl+C` no pierde datos.** El menú atrapa la interrupción y guarda antes de salir. Si guardar falla, avisa y sale igual.
- **Primero sin conexión.** La API de frases usa un tiempo máximo de 3 segundos y, si falla, muestra una frase local.

## Cómo lo construí

Este proyecto es parte de mi aprendizaje de Python y de programación orientada a objetos.

- El enunciado (estructura, fases y requisitos) salió de un prompt que le hice a Gemini.
- Fui programando fase por fase con Claude como mentor: me explicaba los conceptos, revisaba mi código y me señalaba los errores. Yo escribía y corregía el código.
- `main.py` y la primera versión de este README me los dio la IA ya escritos. Los revisé línea por línea hasta poder explicarlos con mis palabras.
- Trabajé con ramas y pull requests, y el historial de commits muestra el proceso real, con sus correcciones.