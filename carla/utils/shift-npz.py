import os
import glob
import shutil

def move_npz_files(source_folders):
    for source_folder in source_folders:
        npz_files = glob.glob(os.path.join(source_folder, '*.npz'))
        destination_folder = os.path.join(source_folder, 'npz')
        print(source_folder, destination_folder)
        os.makedirs(destination_folder, exist_ok=True)
        for npz_file in npz_files:
            shutil.move(npz_file, destination_folder)

if __name__ == "__main__":
    source_folders = [
        "/home/apg/manideep/carla/out/ego-d5/ego0/annotations/dvs/dvs_camera-back",
        "/home/apg/manideep/carla/out/ego-d5/ego0/annotations/dvs/dvs_camera-back-left",
        "/home/apg/manideep/carla/out/ego-d5/ego0/annotations/dvs/dvs_camera-back-right",
        "/home/apg/manideep/carla/out/ego-d5/ego0/annotations/dvs/dvs_camera-front",
        "/home/apg/manideep/carla/out/ego-d5/ego0/annotations/dvs/dvs_camera-front-left",
        "/home/apg/manideep/carla/out/ego-d5/ego0/annotations/dvs/dvs_camera-front-right",

    ]
    move_npz_files(source_folders)
