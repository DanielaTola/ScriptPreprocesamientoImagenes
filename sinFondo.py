import os
from PIL import Image
import pixellib
from pixellib.tune_bg import alter_bg

quitar_fondo = alter_bg()

# Establecer la ruta del directorio de entrada y de salida
input_dir = "C:/Users/Daniela/Desktop/Nuevos videos/IMG-Renderizadas"
output_dir = "C:/Users/Daniela/Desktop/Nuevos videos/Sin-Fondos-9"

# Asegurarse de que el directorio de salida exista, si no, crearlo
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Definir la variable cambiar_fondo
cambiar_fondo = alter_bg()

# Recorrer todas las imágenes en el directorio de entrada y aplicar la técnica de eliminación de fondo
for filename in os.listdir(input_dir):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)
        cambiar_fondo.load_pascalvoc_model("deeplabv3_xception_tf_dim_ordering_tf_kernels.h5")
        cambiar_fondo.color_bg(input_path, colors = (0, 255, 0), output_image_name=output_path, detect="person")
