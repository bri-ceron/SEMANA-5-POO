# Sistema de Gestión de Restaurante.

## 👩‍🎓 Estudiante.

BRIGGITTE DAYANARA CERON RAMOS.

## Descripción del proyecto.

Mi proyecto fue desarrollado como parte de la Tarea de la Semana 5 de la asignatura Programación Orientada a Objetos.

El sistema representa la gestión básica de un restaurante utilizando los principios fundamentales de la Programación Orientada a Objetos (POO) en Python. Su objetivo es administrar productos y clientes mediante clases, objetos y listas, organizando el código de forma modular para facilitar su comprensión, mantenimiento y reutilización.

El programa permite registrar productos y clientes, almacenarlos dentro del restaurante y mostrar la información registrada de manera clara y organizada en la consola.

## Estructura del proyecto

```text
restaurante_app/
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── cliente.py
│
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
│
├── main.py
│
└── README.md
```

# 🏗️ Explicación de la estructura.

El proyecto está organizado en módulos para mejorar la claridad del código y facilitar su mantenimiento.

## 📁 Carpeta **modelos**

Contiene las clases principales del sistema.

- **producto.py:** representa los productos disponibles en el restaurante mediante la clase `Producto`, donde se almacenan atributos como nombre, precio, categoría y disponibilidad.

- **cliente.py:** representa la información de los clientes mediante la clase `Cliente`, incluyendo datos como nombre, edad, correo electrónico y si es un cliente frecuente.

## 📁 Carpeta **servicios**

Contiene la lógica principal del sistema.

- **restaurante.py:** define la clase `Restaurante`, encargada de administrar las listas de productos y clientes mediante métodos para agregar y mostrar la información registrada.

## 📄 Archivo **main.py**

Es el punto de inicio del programa.

En este archivo se crean los objetos de las clases `Producto` y `Cliente`, se agregan al restaurante utilizando los métodos correspondientes y finalmente se presenta toda la información almacenada en la consola.

---

# 💻 Tipos de datos utilizados

| Tipo de dato | Uso dentro del proyecto |
|--------------|-------------------------|
| **str** | Se utiliza para almacenar nombres de productos, categorías, nombres de clientes y correos electrónicos. |
| **int** | Se utiliza para representar la edad del cliente. |
| **float** | Se emplea para almacenar el precio de los productos. |
| **bool** | Permite indicar si un producto está disponible y si un cliente es frecuente. |
| **list** | Se utiliza para almacenar múltiples objetos de tipo `Producto` y `Cliente` dentro de la clase `Restaurante`. |

# 📝 Reflexión

El desarrollo de este proyecto permitió comprender la importancia de aplicar buenas prácticas de programación desde las primeras etapas del desarrollo de software. Utilizar identificadores descriptivos facilita la lectura, comprensión y mantenimiento del código, ya que permite identificar fácilmente la función de cada variable, atributo o método.

Asimismo, seleccionar tipos de datos adecuados garantiza un manejo correcto de la información, evitando errores y haciendo que el programa sea más eficiente y organizado. Finalmente, el uso de listas dentro de un proyecto modular permite administrar múltiples objetos de manera sencilla, favoreciendo la reutilización del código y una mejor estructura de la aplicación. Estos principios son fundamentales para desarrollar programas más claros, escalables y fáciles de mantener.

---

# 👩‍💻 Autor

**Briggitte Dayanara Cerón Ramos**

**Universidad Estatal Amazónica**

**Carrera:** Tecnologías de la Información

**Asignatura:** Programación Orientada a Objetos

**Tarea Semana 5

