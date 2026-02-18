import os
import shutil
from pathlib import Path

# --- CONFIGURACIÓN DE CATEGORÍAS ---
# Puedes añadir más si usas programas específicos
EXTENSIONES = {
    "Imágenes":     ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg', '.bmp', '.tiff', '.ico'],
    "Documentos":   ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.xls', '.pptx', '.ppt', '.csv', '.md'],
    "Audio":        ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma'],
    "Video":        ['.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv', '.webm'],
    "Comprimidos":  ['.zip', '.rar', '.7z', '.tar', '.gz', '.iso'],
    "Instaladores": ['.exe', '.msi', '.bat', '.sh', '.apk', '.dmg'],
    "Código":       ['.py', '.java', '.js', '.html', '.css', '.cpp', '.c', '.sql', '.json', '.xml'],
    "Photoshop":    ['.psd', '.ai'],
    "Torrents":     ['.torrent']
}

def obtener_ruta_descargas():
    """Detecta automáticamente la carpeta de descargas del usuario."""
    return str(Path.home() / "Downloads")

def generar_nombre_unico(ruta_destino):
    """
    Si el archivo ya existe, le añade un número (ej: foto_1.jpg).
    Evita sobrescribir archivos importantes.
    """
    if not os.path.exists(ruta_destino):
        return ruta_destino
    
    nombre, extension = os.path.splitext(ruta_destino)
    contador = 1
    while os.path.exists(f"{nombre}_{contador}{extension}"):
        contador += 1
    
    return f"{nombre}_{contador}{extension}"

def organizar_descargas():
    ruta_base = obtener_ruta_descargas()
    print(f"--- Organizando carpeta: {ruta_base} ---")

    # Comprobamos que la carpeta exista
    if not os.path.exists(ruta_base):
        print("Error: No encuentro la carpeta de Descargas.")
        return

    archivos_movidos = 0
    
    # Recorremos todos los archivos en Descargas
    for archivo in os.listdir(ruta_base):
        ruta_origen = os.path.join(ruta_base, archivo)

        # 1. Ignorar si es una carpeta (solo movemos archivos sueltos)
        if os.path.isdir(ruta_origen):
            continue
            
        # 2. Ignorar archivos ocultos o temporales (empiezan por .)
        if archivo.startswith('.'):
            continue

        # 3. Obtener extensión
        _, extension = os.path.splitext(archivo)
        extension = extension.lower() # Convertir a minúsculas para comparar

        carpeta_destino = "Otros" # Por defecto
        encontrado = False

        # 4. Buscar a qué categoría pertenece
        for carpeta, lista_ext in EXTENSIONES.items():
            if extension in lista_ext:
                carpeta_destino = carpeta
                encontrado = True
                break
        
        # 5. Mover el archivo (si tiene categoría o si decidimos mover los 'Otros')
        if encontrado: 
            # Crear carpeta destino dentro de Descargas (ej: Descargas/Imágenes)
            ruta_carpeta_dest = os.path.join(ruta_base, carpeta_destino)
            os.makedirs(ruta_carpeta_dest, exist_ok=True)

            ruta_final = os.path.join(ruta_carpeta_dest, archivo)
            
            # ¡MAGIA! Gestionar nombres duplicados
            ruta_final_unica = generar_nombre_unico(ruta_final)
            
            try:
                shutil.move(ruta_origen, ruta_final_unica)
                print(f"✅ {archivo} -> {carpeta_destino}")
                archivos_movidos += 1
            except Exception as e:
                print(f"❌ Error moviendo {archivo}: {e}")

    print(f"\n¡Listo! Se han organizado {archivos_movidos} archivos.")

if __name__ == "__main__":
    organizar_descargas()
    input("Presiona ENTER para salir...")