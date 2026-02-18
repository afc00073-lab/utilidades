import os
import shutil

def limpiar_temporales():
    # Detectamos la ruta %TEMP% de tu usuario
    carpeta_temp = os.getenv('TEMP')
    
    print(f"--- LIMPIEZA DE DISCO ---")
    print(f"Analizando ruta: {carpeta_temp}")
    
    confirmacion = input("¿Estás seguro de borrar los archivos temporales? (S/N): ")
    if confirmacion.lower() != 's':
        print("Operación cancelada.")
        return

    archivos_borrados = 0
    espacio_liberado = 0 # (Es difícil calcular exacto, pero contaremos archivos)

    contenido = os.listdir(carpeta_temp)
    total_items = len(contenido)

    print(f"Encontrados {total_items} elementos. Iniciando limpieza...")

    for item in contenido:
        ruta_completa = os.path.join(carpeta_temp, item)

        try:
            if os.path.isfile(ruta_completa):
                os.remove(ruta_completa) # Borrar archivo
                archivos_borrados += 1
            elif os.path.isdir(ruta_completa):
                shutil.rmtree(ruta_completa) # Borrar carpeta entera
                archivos_borrados += 1
                
        except PermissionError:
            # Esto es NORMAL. Si un archivo está abierto, Windows no deja borrarlo.
            # Simplemente lo ignoramos y pasamos al siguiente.
            pass 
        except Exception as e:
            print(f"Error raro en {item}: {e}")

    print("-" * 30)
    print(f"✅ ¡Limpieza terminada!")
    print(f"🗑️  Se han eliminado {archivos_borrados} archivos/carpetas basura.")
    print(f"⚠️  Los archivos que no se borraron estaban en uso por programas abiertos.")
    input("Pulsa ENTER para salir...")

if __name__ == "__main__":
    limpiar_temporales()