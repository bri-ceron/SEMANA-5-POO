# Importamos las clases necesarias.
from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


# Crear el restaurante
restaurante = Restaurante("Restaurante El Buen Sabor")


# Crear productos
producto1 = Producto(
    "Pizza Familiar",
    15.99,
    "Comida",
    True
)

producto2 = Producto(
    "Jugo Natural",
    3.50,
    "Bebida",
    True
)


# Crear clientes
cliente1 = Cliente(
    "Juan Pérez",
    25,
    "juan.perez@gmail.com",
    True
)

cliente2 = Cliente(
    "María López",
    30,
    "maria.lopez@gmail.com",
    False
)


# Agregar productos al restaurante
restaurante.agregar_producto(producto1)
restaurante.agregar_producto(producto2)


# Agregar clientes al restaurante
restaurante.agregar_cliente(cliente1)
restaurante.agregar_cliente(cliente2)


# Mostrar la información del restaurante
print("=" * 45)
print(restaurante.nombre)
print("=" * 45)

restaurante.mostrar_productos()
restaurante.mostrar_clientes()