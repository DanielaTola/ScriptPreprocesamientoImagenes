import cv2
import os

# Directorios de entrada y salida
input_dir = "F:/Nuevos videos/videos/TrainResNet/data completa/TrainNuevoTratamiento/SuavizadoF/Etapa3"
output_dir = "F:/Nuevos videos/videos/TrainResNet/data completa/TrainNuevoTratamiento/SegmentacionDeteccionBordes/Etapa3"


# Crear el directorio de salida si no existe
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Obtener la lista de archivos en el directorio de entrada
files = os.listdir(input_dir)

# Procesar cada archivo en el directorio de entrada
for filename in files:
    # Leer la imagen original
  img = cv2.imread(os.path.join(input_dir, filename))

  # Obtener los canales de la imagen
  blue_channel, green_channel, red_channel = cv2.split(img)

  # Aplicar el filtro de Sobel para detección de bordes
  sobelx = cv2.Sobel(green_channel, cv2.CV_64F, 1, 0, ksize=3)
  sobely = cv2.Sobel(green_channel, cv2.CV_64F, 0, 1, ksize=3)
  edges = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)

  # Combinar los bordes con los canales de color de la imagen original
  result = cv2.merge((cv2.convertScaleAbs(edges), blue_channel, red_channel))

  # Guardar la imagen resultante en el directorio de salida con el mismo nombre
  cv2.imwrite(os.path.join(output_dir, filename), result)
