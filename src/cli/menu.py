ANCHO_BARRA = 16


def renderizar_barra(porcentaje: float) -> str:
    porcentaje = max(0, min(porcentaje, 100))
    llenos = int((porcentaje * ANCHO_BARRA) / 100)
    vacios = ANCHO_BARRA - llenos
    return f"[{"█"* llenos}{"░"*vacios}] {porcentaje:.1f}%"



def pedir_numero(mensaje: str) -> float:
    while True:
        texto = input(mensaje).strip()        
        try:
            numero = float(texto.replace(",", "."))
        except ValueError:
            print("Escribe un número válido.")
            continue
        if numero <= 0:
            print("Debe ser mayor que 0.")
            continue
        return numero

