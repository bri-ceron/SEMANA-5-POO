# Clase que representa un cliente del restaurante.

class Cliente:
    def __init__(self, nombre: str, edad: int, correo: str, cliente_frecuente: bool):
        # Inicializa los atributos del cliente
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
        self.cliente_frecuente = cliente_frecuente

    def __str__(self):
        # Devuelve la información del cliente en formato de texto
        tipo = "Cliente frecuente" if self.cliente_frecuente else "Cliente nuevo"

        return (
            f"Cliente: {self.nombre} | "
            f"Edad: {self.edad} años | "
            f"Correo: {self.correo} | "
            f"{tipo}"
        )