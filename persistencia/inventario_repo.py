class InventarioRepository:
    def __init__(self, ruta='inventario.txt'):
        self.ruta = ruta

    def cargar(self):
        try:
            with open(self.ruta, 'r', encoding='utf-8') as f:
                return f.readlines()
        except FileNotFoundError:
            return []

    def guardar(self, lineas):
        with open(self.ruta, 'w', encoding='utf-8') as f:
            f.write('\n'.join(linea.rstrip('\n') for linea in lineas))
            if lineas:
                f.write('\n')
