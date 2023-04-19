import cv2
import os
import shutil

# Establecer la ruta del directorio de entrada y de salida
input_dir = "F:/Nuevos videos/videos/TrainResNet/data completa/Etapa4"
output_dir = "C:/Users/Daniela/Desktop/Utimo DataSet/DA/Etapa4"

# Crear el directorio de salida si no existe
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for filename in os.listdir(input_dir):
    # Cargar la imagen
    img = cv2.imread(os.path.join(input_dir, filename))
    
    # Rotar la imagen -90 grados
    #rotated_img1 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
    
    # Rotar la imagen 180 grados
    rotated_img2 = cv2.rotate(img, cv2.ROTATE_180)

    # Renombrar la imagen
    #new_filename = "DA-" + filename
    #new_filename = "DA-90-" + filename
    new_filename = "DA-180-" + filename
    new_path = os.path.join(output_dir, new_filename)
    
    # Escribir la imagen rotada en el directorio de salida
    #cv2.imwrite(new_path, img)
    #cv2.imwrite(new_path, rotated_img1)
    cv2.imwrite(new_path, rotated_img2)
    