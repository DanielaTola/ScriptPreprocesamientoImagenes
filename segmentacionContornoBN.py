import cv2
import numpy as np
import os

# Establecer la ruta del directorio de entrada y de salida
input_dir = "C:/Users/Daniela/Desktop/Utimo DataSet/Normalizado-Renderizado/Etapa1"
output_dir = "C:/Users/Daniela/Desktop/Utimo DataSet/Contornos/Etapa1"

# crear el directorio de salida si no existe
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# definir el umbral para la detección de bordes
threshold1 = 30
threshold2 = 100

# recorrer cada archivo en el directorio de entrada
for filename in os.listdir(input_dir):
    # abrir la imagen en escala de grises usando OpenCV
    img = cv2.imread(os.path.join(input_dir, filename), cv2.IMREAD_GRAYSCALE)

    # aplicar el algoritmo de Canny para detectar los bordes
    edges = cv2.Canny(img, threshold1, threshold2)

    # crear una imagen nueva con los bordes resaltados en verde
    result = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    result[np.where(edges != 0)] = [0, 255, 0]

    # guardar la imagen procesada en el directorio de salida
    cv2.imwrite(os.path.join(output_dir, filename), result)
