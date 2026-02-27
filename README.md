# Sistema Avanzado de Gestion de Inventario

## Descripcion
Aplicacion de consola en Python para gestionar productos de inventario con Programacion Orientada a Objetos (POO), uso de colecciones y persistencia en archivos.

## Estructura
- `modelos/producto.py`: clase `Producto`.
- `servicios/inventarioservice.py`: clase `Inventario` (y alias `InventarioService`).
- `persistencia/inventario_repo.py`: clase `InventarioRepository` para lectura/escritura.
- `main.py`: menu interactivo de consola.

## Requisitos de la tarea y como se cumplen
1. POO
- Se usan clases separadas por responsabilidad (`Producto`, `Inventario`, `InventarioRepository`).

2. Colecciones
- `dict` (`Inventario.productos`): acceso rapido por ID.
- `set` (`Inventario.ids`): validacion de IDs unicos.
- `list`: resultados de busqueda y exportacion de lineas.
- `tuple` (`Producto._id_nombre`): agrupacion de ID y nombre.

3. Almacenamiento en archivos
- `InventarioRepository.cargar()`: deserializa lineas del archivo.
- `InventarioRepository.guardar()`: serializa el inventario en `inventario.txt`.
- `Producto.to_line()` y `Producto.from_line()` manejan formato `id;nombre;cantidad;precio`.

4. Interfaz de usuario
- Menu en consola con: agregar, eliminar, actualizar, buscar, mostrar, guardar y salir.

## Pruebas funcionales realizadas
1. Crear producto y agregarlo al inventario.
2. Intentar agregar ID repetido (lanza `ValueError`).
3. Actualizar cantidad/precio por ID existente.
4. Buscar por nombre parcial sin distinguir mayusculas.
5. Guardar en archivo y volver a cargar.
6. Eliminar producto por ID.

## Ejecucion
```bash
python main.py
```

## Nota
Para entregar en Moodle/GitHub, sube este proyecto con este README y evidencia de ejecucion (capturas o salida de consola).
