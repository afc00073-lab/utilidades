#Debes instalar python -m pip install yt-dlp en terminal para que funcione este programa
import os
import yt_dlp

def descargar_videos():
    # 1. Creamos la carpeta para guardar los videos
    carpeta_destino = "Videos_Descargados"
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)

    print("--- BAJAVIDEOS 3000 ---")
    print("Pega los enlaces de YouTube (escribe 'SALIR' para terminar):")

    while True:
        url = input(">> Enlace: ")
        if url.lower() == 'salir':
            break

        # Configuración de yt-dlp
        opciones = {
            'format': 'best', # Descarga la mejor calidad disponible (video+audio)
            'outtmpl': os.path.join(carpeta_destino, '%(title)s.%(ext)s'), # Nombre del archivo
            'noplaylist': True, # Si es una lista, baja solo el video (cambiar a False si quieres la lista)
        }

        print(f"⏳ Descargando: {url}...")
        
        try:
            with yt_dlp.YoutubeDL(opciones) as ydl:
                ydl.download([url])
            print("✅ ¡Descarga completada!")
        except Exception as e:
            print(f"❌ Error descargando: {e}")

if __name__ == "__main__":
    descargar_videos()