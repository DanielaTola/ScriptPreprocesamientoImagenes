from PIL import Image, ImageEnhance
import os

input_dir = "C:/Users/Daniela/Desktop/Utimo DataSet/DA/Etapa1"
output_dir = "C:/Users/Daniela/Desktop/Utimo DataSet/Nitidez/Etapa1"

if not os.path.exists(output_dir):
  os.makedirs(output_dir)


for i, filename in enumerate(os.listdir(input_dir)):
  
  imagen = Image.open(os.path.join(input_dir, filename))

  # Aumentar nitidez de la imagen
  aumento_nitidez = 3.0
  enhancer = ImageEnhance.Sharpness(imagen)
  imagen_nitida = enhancer.enhance(aumento_nitidez)

  # Cambiar nombre de la imagen
  nombre_nuevo = f"IMG-ETAPA-01-{i}.jpg"

  # Guardar imagen rotada y mejorada con el nuevo nombre
  imagen_nitida.save(os.path.join(output_dir, nombre_nuevo))
