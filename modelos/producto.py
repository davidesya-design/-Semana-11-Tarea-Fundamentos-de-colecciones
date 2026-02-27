# Clase que representa un producto del inventario.
# Incluye getters/setters para cumplir con la rubrica.


class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self._id_nombre = (id_producto, nombre)
        self._cantidad = 0
        self._precio = 0.0
        self.set_cantidad(cantidad)
        self.set_precio(precio)

    # Getters explicitos
    def get_id(self):
        return self._id_nombre[0]

    def get_nombre(self):
        return self._id_nombre[1]

    def get_cantidad(self):
        return self._cantidad

    def get_precio(self):
        return self._precio

    # Setters explicitos
    def set_id(self, nuevo_id):
        if not str(nuevo_id).strip():
            raise ValueError("El ID no puede estar vacio")
        self._id_nombre = (str(nuevo_id).strip(), self.get_nombre())

    def set_nombre(self, nuevo_nombre):
        if not str(nuevo_nombre).strip():
            raise ValueError("El nombre no puede estar vacio")
        self._id_nombre = (self.get_id(), str(nuevo_nombre).strip())

    def set_cantidad(self, nueva_cantidad):
        cantidad = int(nueva_cantidad)
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
        self._cantidad = cantidad

    def set_precio(self, nuevo_precio):
        precio = float(nuevo_precio)
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio = precio

    # Properties para uso comodo en el resto del sistema
    @property
    def id(self):
        return self.get_id()

    @property
    def nombre(self):
        return self.get_nombre()

    @property
    def cantidad(self):
        return self.get_cantidad()

    @cantidad.setter
    def cantidad(self, valor):
        self.set_cantidad(valor)

    @property
    def precio(self):
        return self.get_precio()

    @precio.setter
    def precio(self, valor):
        self.set_precio(valor)

    # Serializacion simple en una linea de texto
    def to_line(self):
        return f"{self.id};{self.nombre};{self.cantidad};{self.precio}"

    @staticmethod
    def from_line(linea):
        partes = linea.strip().split(";")
        if len(partes) != 4:
            raise ValueError("Linea de producto invalida")
        return Producto(partes[0], partes[1], int(partes[2]), float(partes[3]))

    def __str__(self):
        return f"ID:{self.id} | {self.nombre} | Stock:{self.cantidad} | ${self.precio:.2f}"
