import os
import shutil


input_dir = "F:/Caracterizado/Etapa4"
output_dir = "C:/Users/Daniela/Desktop/Utimo DataSet/Renombradas/Etapa4"

# crear el directorio de salida si no existe
if not os.path.exists(output_dir):
    os.makedirs(output_dir)



count = 0
for file_name in os.listdir(input_dir):
    if file_name.endswith(".jpg"):
        old_path = os.path.join(input_dir, file_name)
        new_name = "IMAG-ETAPA-3-" + str(count) + ".jpg"
        new_path = os.path.join(output_dir, new_name)
        shutil.copyfile(old_path, new_path)
        count += 1