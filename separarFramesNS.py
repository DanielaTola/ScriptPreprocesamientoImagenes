import cv2
import os

video_folder = 'C:/Users/Daniela/Desktop/videos'
frame_folder = 'C:/Users/Daniela/Desktop/Nuevos videos'
time_interval = 3

if not os.path.exists(frame_folder):
    os.makedirs(frame_folder)

for file_name in os.listdir(video_folder):
    if not file_name.endswith('.mp4'):
        continue

    video_path = os.path.join(video_folder, file_name)
    video = cv2.VideoCapture(video_path)
    fps = video.get(cv2.CAP_PROP_FPS)
    frame_count = 0
    time_count = 0

    while True:
        ret, frame = video.read()
        if not ret:
            break

        if time_count < time_interval:
            time_count += 1/fps
            continue

        frame_name = f'{os.path.splitext(file_name)[0]}_{frame_count:04}.jpg'
        frame_path = os.path.join(frame_folder, frame_name)

        cv2.imwrite(frame_path, frame)
        frame_count += 1
        time_count = 0
    
    video.release()
