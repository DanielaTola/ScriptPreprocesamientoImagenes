import cv2
import os

# Establecer la ruta del directorio de entrada y de salida
input_dir = "C:/Users/Daniela/Desktop/Utimo DataSet/Nitidez/Etapa4"
output_dir = "C:/Users/Daniela/Desktop/Utimo DataSet/SegContorno/Etapa4"

# Crear el directorio de salida si no existe
if not os.path.exists(output_dir):
    os.makedirs(output_dir)


# Crear el directorio de salida si no existe
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Iterar sobre las imágenes en el directorio de entrada
for filename in os.listdir(input_dir):
    # Cargar la imagen
    img = cv2.imread(os.path.join(input_dir, filename))
    
    # Convertir la imagen a escala de grises
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Aplicar umbralización adaptativa de Otsu
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)[1]

    # Encontrar los contornos
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Dibujar los contornos en la imagen original
    cv2.drawContours(img, contours, -1, (255, 255, 0), 2)

    # Escribir la imagen con los contornos dibujados en el directorio de salida
    cv2.imwrite(os.path.join(output_dir, filename), img)

# import cv2
# import numpy as np

# # Cargar la imagen y convertirla a escala de grises
# img = cv2.imread('C:/Users/Daniela/Downloads/Girasol.jpg')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # Aplicar un umbral adaptativo
# thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

# # Encontrar los contornos en la imagen umbralizada
# contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# # Dibujar los contornos en la imagen original
# cv2.drawContours(img, contours, -1, (255, 0, 0), 2)

# # Mostrar la imagen resultante
# cv2.imshow('Image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
