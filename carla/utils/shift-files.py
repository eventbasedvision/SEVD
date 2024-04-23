import os
import shutil

source_folders = [
    "/home/apg/manideep/carla/out/ego-d5/ego0/images/rgb/rgb_camera-back",
    "/home/apg/manideep/carla/out/ego-d5/ego0/images/rgb/rgb_camera-back-left",
    "/home/apg/manideep/carla/out/ego-d5/ego0/images/rgb/rgb_camera-back-right",
    "/home/apg/manideep/carla/out/ego-d5/ego0/images/rgb/rgb_camera-front",
    "/home/apg/manideep/carla/out/ego-d5/ego0/images/rgb/rgb_camera-front-left",
    "/home/apg/manideep/carla/out/ego-d5/ego0/images/rgb/rgb_camera-front-right",
]

print("DVS")
for source_folder in source_folders:
    target_folder = source_folder.replace("rgb", "dvs")
    os.makedirs(target_folder, exist_ok=True)
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.startswith('d'):
                file_path = os.path.join(root, file)
                new_file_path = os.path.join(target_folder, f'{file.replace("dvs-", "")}')
                shutil.move(file_path, new_file_path)

print("CALIB")
for source_folder in source_folders:
    target_folder = source_folder.replace("rgb", "calibration")
    os.makedirs(target_folder, exist_ok=True)
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.startswith('calib'):
                file_path = os.path.join(root, file)
                new_file_path = os.path.join(target_folder, f'{file.replace("calib-", "")}')
                shutil.move(file_path, new_file_path)
print("Files moved successfully.")
