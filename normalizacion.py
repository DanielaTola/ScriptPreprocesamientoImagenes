import cv2
import os
input_images_path = "F:/Nuevos videos/videos/TrainResNet/data completa/Etapa2"
files_names = os.listdir(input_images_path)
print(files_names)
output_images_path = "F:/Nuevos videos/videos/TrainResNet/data completa/Re-Entrenado/ETAPA2"
if not os.path.exists(output_images_path):
    os.makedirs(output_images_path)
    print("Directorio creado: ", output_images_path)
count = 0
for file_name in files_names:
    image_path = input_images_path + "/" + file_name
    print(image_path)
    image = cv2.imread(image_path)
    if image is None:
        continue
    #RENDERIZA
    #image = cv2.resize(image, (380, 460), interpolation=cv2.INTER_CUBIC)
    #NROMALIZA
    image_norm = cv2.normalize(image, None, alpha=1,beta=500, norm_type=cv2.NORM_MINMAX)
    #RENOMBRA
    cv2.imwrite(output_images_path + "/IMG-ESTAPA-02-" + str(count+1) + ".jpg", image)
    count += 1
