import numpy as np
import os
from tqdm import tqdm
import time


input_directories = [
    '/Users/manideepreddyaliminati/Documents/coding/research/data-fix/data/FIXED/1/fixed-1',
    '/Users/manideepreddyaliminati/Documents/coding/research/data-fix/data/FIXED/1/fixed-2',
    '/Users/manideepreddyaliminati/Documents/coding/research/data-fix/data/FIXED/1/fixed-3',
    '/Users/manideepreddyaliminati/Documents/coding/research/data-fix/data/FIXED/1/fixed-4',

    '/Users/manideepreddyaliminati/Documents/coding/research/data-fix/data/FIXED/2/fixed-5',
    '/Users/manideepreddyaliminati/Documents/coding/research/data-fix/data/FIXED/2/fixed-6',
    '/Users/manideepreddyaliminati/Documents/coding/research/data-fix/data/FIXED/2/fixed-7',
    '/Users/manideepreddyaliminati/Documents/coding/research/data-fix/data/FIXED/2/fixed-8',
]
for input_directory in input_directories:
    num = input_directory.split('/')[-2]
    result = input_directory.split('/')[-1]
    type = input_directory.split('/')[-3]

    all_files = sorted([filename for filename in os.listdir(input_directory) if filename.endswith(".npz")],
                       key=lambda x: int(x.split('-')[0]))

    compiled_output_file_path = f'/Users/manideepreddyaliminati/Documents/coding/research/data-fix/data/{type}/{num}/compiled-{result}.npz'
    compiled_data = {}
    for filename in tqdm(all_files, desc=f"Processing files {num}-{result}"):
        if filename.endswith(".npz"):
            file_path = os.path.join(input_directory, filename)
            file_number = str(filename.split('-')[0])
            try:
                loaded_data = np.load(file_path)
                dvs_events = loaded_data['dvs_events']
                compiled_data[file_number] = dvs_events
                del loaded_data, dvs_events
            except Exception as e:
                print(f"Error processing {filename}: {e}")

    start = time.time()
    np.savez_compressed(compiled_output_file_path, **compiled_data)
    end = time.time()
    print(end - start, "s")

    # compiled_output_file_path = f'/Users/manideepreddyaliminati/Documents/coding/research/data-fix/data/EGO/{num}/compiled-{result}-1.npz'
    # compiled_data = {}
    # for filename in tqdm(all_files[:1000], desc=f"Processing files {num}-{result}"):
    #     if filename.endswith(".npz"):
    #         file_path = os.path.join(input_directory, filename)
    #         file_number = str(filename.split('-')[0])
    #         try:
    #             loaded_data = np.load(file_path)
    #             dvs_events = loaded_data['dvs_events']
    #             compiled_data[file_number] = dvs_events
    #             del loaded_data, dvs_events
    #         except Exception as e:
    #             print(f"Error processing {filename}: {e}")

    # start = time.time()
    # np.savez_compressed(compiled_output_file_path, **compiled_data)
    # end = time.time()
    # print(end - start, "s")

    # compiled_output_file_path = f'/Users/manideepreddyaliminati/Documents/coding/research/data-fix/data/EGO/{num}/compiled-{result}-2.npz'
    # compiled_data = {}
    # for filename in tqdm(all_files[1000:1900], desc=f"Processing files {num}-{result}"):
    #     if filename.endswith(".npz"):
    #         file_path = os.path.join(input_directory, filename)
    #         file_number = str(filename.split('-')[0])
    #         try:
    #             loaded_data = np.load(file_path)
    #             dvs_events = loaded_data['dvs_events']
    #             compiled_data[file_number] = dvs_events
    #             del loaded_data, dvs_events
    #         except Exception as e:
    #             print(f"Error processing {filename}: {e}")

    # start = time.time()
    # np.savez_compressed(compiled_output_file_path, **compiled_data)
    # end = time.time()
    # print(end - start, "s")

    # compiled_output_file_path = f'/Users/manideepreddyaliminati/Documents/coding/research/data-fix/data/EGO/{num}/compiled-{result}-3.npz'
    # compiled_data = {}
    # for filename in tqdm(all_files[1900:], desc=f"Processing files {num}-{result}"):
    #     if filename.endswith(".npz"):
    #         file_path = os.path.join(input_directory, filename)
    #         file_number = str(filename.split('-')[0])
    #         try:
    #             loaded_data = np.load(file_path)
    #             dvs_events = loaded_data['dvs_events']
    #             compiled_data[file_number] = dvs_events
    #             del loaded_data, dvs_events
    #         except Exception as e:
    #             print(f"Error processing {filename}: {e}")

    # start = time.time()
    # np.savez_compressed(compiled_output_file_path, **compiled_data)
    # end = time.time()
    # print(end - start, "s")
