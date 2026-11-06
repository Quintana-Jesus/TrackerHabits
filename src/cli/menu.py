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