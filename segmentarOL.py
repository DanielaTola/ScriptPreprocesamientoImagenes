import os
import cv2
from PIL import Image
import numpy as np

def remove_background(input_dir, output_dir):
    for dirpath, dirnames, filenames in os.walk(input_dir):
        for filename in filenames:
            if not filename.endswith('.jpg'):
                continue

            # Cargar imagen
            img_path = os.path.join(dirpath, filename)
            img = cv2.imread(img_path)

            # Convertir a escala de grises
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Aplicar umbralización adaptativa
            thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

            # Aplicar operación morfológica de cierre
            kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
            closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

            # Encontrar contornos
            contours, hierarchy = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            # Crear máscara negra del mismo tamaño que la imagen original
            mask = np.zeros_like(img)

            # Dibujar contornos en la máscara blanca
            for contour in contours:
                cv2.drawContours(mask, [contour], 0, (255, 255, 255), -1)

            # Aplicar la máscara en la imagen original
            masked_image = cv2.bitwise_and(img, mask)

            # Guardar la imagen segmentada
            output_path = os.path.join(output_dir, os.path.relpath(img_path, input_dir))
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            cv2.imwrite(output_path, masked_image)
            
            # Imprimir información para verificar que todo está funcionando correctamente
            print(f"Imagen procesada: {img_path}")
            print(f"Imagen guardada en: {output_path}")

input_dir = "F:/Nuevos videos/videos/TrainResNet/data completa/TrainNuevoTratamiento/SuavizadoF/Etapa1"
output_dir = "F:/Nuevos videos/videos/TrainResNet/data completa/TrainNuevoTratamiento/OtroSegmento/Estapa1"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)


remove_background(input_dir, output_dir)
