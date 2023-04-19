from PIL import Image
import os

input_dir = "C:/Users/Daniela/Desktop/Utimo DataSet/SegHistograma/Etapa1"
output_dir = "C:/Users/Daniela/Desktop/Utimo DataSet/RenderizarHistograma/Etapa1"

# crear el directorio de salida si no existe
if not os.path.exists(output_dir):
  os.makedirs(output_dir)


# tamaño deseado
desired_size = (226, 256)

# recorrer cada archivo en el directorio de entrada
for filename in os.listdir(input_dir):
    # abrir la imagen usando Pillow
  with Image.open(os.path.join(input_dir, filename)) as img:
      # ajustar el tamaño de la imagen
      resized_img = img.resize(desired_size)

        # guardar la imagen procesada en el directorio de salida
      resized_img.save(os.path.join(output_dir, filename))
