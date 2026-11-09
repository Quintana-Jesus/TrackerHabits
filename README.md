# PulseHabits CLI

Aplicación de consola en Python para llevar el seguimiento de hábitos de bienestar: defines tus hábitos con una meta diaria, registras tu progreso y ves tu avance en una barra de progreso. Está construida con una arquitectura en capas (modelos, servicios y CLI) y funciona sin conexión a internet.

## Qué hace

- **Ver resumen del día:** hábitos totales, completados y pendientes, con una barra de progreso global.
- **Registrar progreso:** suma una cantidad a un hábito y avisa cuando alcanzas la meta.
- **Crear y eliminar hábitos:** sin distinguir mayúsculas y sin permitir nombres repetidos.
- **Frase motivacional:** consulta la API pública de [ZenQuotes](https://zenquotes.io); si no hay internet, muestra una frase local.
- **Guardado automático:** los datos se guardan en un archivo JSON al salir, incluso si interrumpes el programa con `Ctrl+C`.

## Tecnologías

- Python 3.9 o superior
- [requests](https://pypi.org/project/requests/) para consumir la API
- [pytest](https://pytest.org) para las pruebas
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

Para correr las pruebas:

```bash
python -m pytest
```

## Estructura del proyecto

```
TrackerHabits/
├── data/                  # rutina.json (se genera al guardar, no se sube al repo)
├── src/
│   ├── models/
│   │   ├── habito.py      # entidad Habito
│   │   └── usuario.py     # entidad Usuario y su rutina
│   ├── services/
│   │   ├── storage.py     # lectura y escritura del JSON
│   │   └── quote_service.py  # frase motivacional (API con respaldo local)
│   └── cli/
│       └── menu.py        # menú interactivo en consola
├── tests/
│   ├── test_habito.py
│   └── test_usuario.py
├── main.py                # punto de entrada
├── requirements.txt
└── README.md
```