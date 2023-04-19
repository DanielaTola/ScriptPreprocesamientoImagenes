import os
from PIL import Image

# Establecer la ruta del directorio de entrada y de salida
input_dir = "F:/Nuevos videos/videos/TrainResNet/data completa/TrainNuevoTratamiento/SuavizadoF"
output_dir = "F:/Nuevos videos/videos/TrainResNet/data completa/TrainNuevoTratamiento/RecizeSinSegmentar-prueba"

# Recorre todos los archivos en el directorio de entrada y sus subdirectorios
for root, dirs, files in os.walk(input_dir):
    for filename in files:
        # Verifica si el archivo es una imagen
        if filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp")):
            # Establece la ruta completa de la imagen de entrada y salida
            input_path = os.path.join(root, filename)
            output_path = os.path.join(output_dir, os.path.relpath(input_path, input_dir))
            # Crea el directorio de salida si no existe
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            # Abre la imagen, redimensiona y guarda en la nueva ubicación
            with Image.open(input_path) as img:
                img_resized = img.resize((226, 226), resample=Image.BICUBIC)
                img_resized.save(output_path)
