import os
# Primer archivo y fundamental para todo el progrma
from modelos.producto import Producto
from servicios.inventarioservice import Inventario
from persistencia.inventario_repo import InventarioRepository


def main():
    inventario = Inventario()
    repo = InventarioRepository()

    if os.path.exists(repo.ruta):
        print(f"Archivo detectado: {repo.ruta}. Cargando inventario...")
    else:
        print(f"No se encontro {repo.ruta}. Iniciando inventario vacio...")

    inventario.cargar_desde_lineas(repo.cargar())

    while True:
        print("""
===== INVENTARIO =====
1. Agregar producto
2. Eliminar producto
3. Actualizar producto
4. Buscar por nombre
5. Mostrar todos
6. Guardar
7. Salir
""")

        op = input("Opcion: ")

        try:
            if op == "1":
                id_p = input("ID: ").strip()
                nombre = input("Nombre: ").strip()
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))

                inventario.agregar_producto(Producto(id_p, nombre, cantidad, precio))
                print("Producto agregado")

            elif op == "2":
                inventario.eliminar_producto(input("ID: ").strip())
                print("Producto eliminado")

            elif op == "3":
                id_p = input("ID: ").strip()
                cantidad = input("Cantidad (Enter para omitir): ").strip()
                precio = input("Precio (Enter para omitir): ").strip()

                inventario.actualizar_producto(
                    id_p,
                    int(cantidad) if cantidad else None,
                    float(precio) if precio else None,
                )
                print("Producto actualizado")

            elif op == "4":
                nombre = input("Buscar: ")
                resultados = inventario.buscar_por_nombre(nombre)

                if not resultados:
                    print("No se encontraron productos")
                else:
                    for p in resultados:
                        print(p)

            elif op == "5":
                productos = inventario.obtener_todos()

                if not productos:
                    print("Inventario vacio")
                else:
                    for p in productos:
                        print(p)

            elif op == "6":
                repo.guardar(inventario.exportar_lineas())
                print("Datos guardados")

            elif op == "7":
                repo.guardar(inventario.exportar_lineas())
                print("Saliendo del sistema")
                break

            else:
                print("Opcion invalida")

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()

