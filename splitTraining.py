import os
import random
import shutil

src_dir = 'E:/TrainResNet/data completa/Nuevos Train/Train/Etapa4'
dst_dir = 'E:/TrainResNet/data completa/Nuevos Train/Test/Etapa4'

def move_10_percent_files(src_directory, dst_directory):
    files = os.listdir(src_directory)
    number_of_files = len(files)
    ten_percent_files = int(number_of_files * 0.2)
    print("wwww:", ten_percent_files)
    selected_files = random.sample(files, ten_percent_files)
    print("Sss:", len(selected_files))
    os.makedirs(dst_directory, exist_ok=True)
    for file in selected_files:
        src_path = os.path.join(src_directory, file)
        dst_path = os.path.join(dst_directory, file)
        print("Eeee:", dst_path)
        shutil.move(src_path, dst_path)

move_10_percent_files(src_dir, dst_dir)


