import requests

URL_API = "https://zenquotes.io/api/random"
TIMEOUT_SEGUNDOS = 3
FRASE_POR_DEFECTO = "La constancia vence al talento cuando el talento no es constante."


class QuoteService:
    def obtener_frase(self) -> str:
        try:
            respuesta = requests.get(URL_API, timeout=TIMEOUT_SEGUNDOS)
            respuesta.raise_for_status()
            datos = respuesta.json()
            frase = datos[0]["q"]
            autor = datos[0]["a"]
            return f'"{frase}" - {autor}'
        except (requests.RequestException, ValueError, KeyError, IndexError):
            return FRASE_POR_DEFECTO
