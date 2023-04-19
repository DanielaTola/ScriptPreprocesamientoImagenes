import os
import random
import cv2
import numpy as np
from PIL import Image

src_dir = 'E:/TrainResNet/data completa/Nuevos Train/Train/Etapa1'
dst_dir = 'E:/TrainResNet/data completa/Nuevos Train/Test/Etapa1'


img_list = os.listdir(src_dir)
selected_imgs = random.sample(img_list, 122)
count=0

for img_name in selected_imgs:
    count += 1
    img = Image.open(os.path.join(src_dir, img_name))
    # Renderizar la imagen
    #img = img.resize((256, 256), Image.ANTIALIAS)
    # Normalizar la imagen
    #img = (np.array(img) / 255.0).astype(np.float32)
    new_name = 'IMG-ETAPA-01-0'+str(count)+'.jpg'
    print("Image:"+new_name)
    cv2.imwrite(os.path.join(dst_dir, new_name),255.0)