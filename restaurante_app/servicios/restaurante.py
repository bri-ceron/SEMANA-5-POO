# Importamos las clases Producto y Cliente desde la carpeta modelos.
from modelos.producto import Producto
from modelos.cliente import Cliente


# Clase que representa un restaurante.
class Restaurante:
    def __init__(self, nombre: str):
        # Nombre del restaurante
        self.nombre = nombre

        # Lista para almacenar los productos
        self.productos: list[Producto] = []

        # Lista para almacenar los clientes
        self.clientes: list[Cliente] = []

    # Agrega un producto a la lista
    def agregar_producto(self, producto: Producto):
        self.productos.append(producto)

    # Agrega un cliente a la lista
    def agregar_cliente(self, cliente: Cliente):
        self.clientes.append(cliente)

    # Muestra todos los productos registrados
    def mostrar_productos(self):
        print("\n===== PRODUCTOS =====")

        for producto in self.productos:
            print(producto)

    # Muestra todos los clientes registrados
    def mostrar_clientes(self):
        print("\n===== CLIENTES =====")

        for cliente in self.clientes:
            print(cliente)