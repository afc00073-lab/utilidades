# Debes instalar: python -m pip install yt-dlp
# IMPORTANTE: Necesitas tener FFmpeg instalado en tu sistema para la conversión a MP3.

import os
import yt_dlp


def descargar_audios_desde_archivo(nombre_archivo):
    # 1. Creamos la carpeta para guardar los audios
    carpeta_destino = "Audios_MP3_Descargados"
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)

    # 2. Verificamos que el archivo de texto exista
    if not os.path.exists(nombre_archivo):
        print(f"❌ Error: No se encontró el archivo '{nombre_archivo}'.")
        print("Asegúrate de crearlo y poner un enlace por línea.")
        return

    print("--- BAJAAUDIOS 3000 ---")
    print(f"Leyendo enlaces desde: {nombre_archivo}")

    # 3. Configuración de yt-dlp para extraer MP3
    opciones = {
        'format': 'bestaudio/best',  # Descarga la mejor calidad de audio disponible
        'outtmpl': os.path.join(carpeta_destino, '%(title)s.%(ext)s'),
        'noplaylist': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',  # Convierte el formato a mp3
            'preferredquality': '192',  # Calidad de 192 kbps (buen equilibrio entre tamaño y calidad)
        }],
    }

    # 4. Leemos el archivo
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        # Extraemos las líneas y quitamos espacios en blanco o saltos de línea vacíos
        enlaces = [linea.strip() for linea in archivo if linea.strip()]

    if not enlaces:
        print("⚠️ El archivo de texto está vacío.")
        return

    print(f"⏳ Se encontraron {len(enlaces)} enlaces. Iniciando descarga...")

    # 5. Descargamos usando yt-dlp
    try:
        with yt_dlp.YoutubeDL(opciones) as ydl:
            # ydl.download acepta una lista completa de enlaces de una sola vez
            ydl.download(enlaces)
        print("\n✅ ¡Todas las descargas se han completado con éxito!")
    except Exception as e:
        print(f"\n❌ Error durante el proceso de descarga: {e}")


if __name__ == "__main__":
    # Define aquí el nombre de tu archivo de texto
    archivo_texto = "enlaces.txt"
    descargar_audios_desde_archivo(archivo_texto)