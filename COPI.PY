import os
import random
from PIL import Image


src_dir = 'E:/TrainResNet/data completa/Etapa4'
dst_dir = 'E:/TrainResNet/data completa/Nuevos Train/Train/Etapa4'

img_list = os.listdir(src_dir)

# Seleccionar aleatoriamente 122 imágenes
selected_imgs = random.sample(img_list, 122)
count = 1

for img_name in selected_imgs:
    img_path = os.path.join(src_dir, img_name)
    with Image.open(img_path) as img:
        # Copiar la imagen al directorio de destino
        new_name = f'IMG-ETAPA-04-{count:03d}.jpg'
        print(new_name)
        img.save(os.path.join(dst_dir, new_name))
        count += 1
