# Clase que representa un producto del restaurante.

class Producto:
    def __init__(self, nombre: str, precio: float, categoria: str, disponible: bool):
        # Inicializa los atributos del producto
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.disponible = disponible

    def __str__(self):
        # Devuelve la información del producto en formato de texto
        estado = "Disponible" if self.disponible else "No disponible"

        return (
            f"Producto: {self.nombre} | "
            f"Categoría: {self.categoria} | "
            f"Precio: ${self.precio:.2f} | "
            f"Estado: {estado}"
        )

