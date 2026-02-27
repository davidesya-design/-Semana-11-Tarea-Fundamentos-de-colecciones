from modelos.producto import Producto


class Inventario:
    # Clase principal de negocio para administrar el inventario.
    def __init__(self):
        # Diccionario: clave=ID, valor=Producto
        self.productos = {}
        # Conjunto para validar IDs unicos en O(1)
        self.ids = set()

    def agregar_producto(self, producto: Producto):
        if producto.id in self.ids:
            raise ValueError("ID duplicado")
        self.productos[producto.id] = producto
        self.ids.add(producto.id)

    def eliminar_producto(self, id_producto):
        if id_producto not in self.productos:
            raise ValueError("Producto no encontrado")
        del self.productos[id_producto]
        self.ids.discard(id_producto)

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto not in self.productos:
            raise ValueError("Producto no encontrado")

        producto = self.productos[id_producto]
        if cantidad is not None:
            producto.set_cantidad(cantidad)
        if precio is not None:
            producto.set_precio(precio)

    def buscar_por_nombre(self, nombre):
        texto = nombre.lower().strip()
        return [
            p for p in self.productos.values()
            if texto in p.nombre.lower()
        ]

    def obtener_todos(self):
        return list(self.productos.values())

    def cargar_desde_lineas(self, lineas):
        self.productos.clear()
        self.ids.clear()

        for linea in lineas:
            if not linea.strip():
                continue
            producto = Producto.from_line(linea)
            if producto.id in self.ids:
                raise ValueError(f"ID duplicado en archivo: {producto.id}")
            self.productos[producto.id] = producto
            self.ids.add(producto.id)

    def exportar_lineas(self):
        return [p.to_line() for p in self.productos.values()]


# Alias para mantener compatibilidad con codigo previo
InventarioService = Inventario
