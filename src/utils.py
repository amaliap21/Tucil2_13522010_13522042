import os
import glob
import shutil

##### ALGORITMA UPDATE DIRECTORY #####
def update_folder_numbers(base_path):
    folders = {'Brute Force': 1, 'Divide and Conquer': 1}
    for key in folders.keys():
        path = os.path.join(base_path, key)
        if not os.path.exists(path):
            os.makedirs(path)
        existing_folders = next(os.walk(path))[1]
        numbers = [int(folder) for folder in existing_folders if folder.isdigit()]
        folders[key] = max(numbers) + 1 if numbers else 1
    return folders


##### ALGORITMA PEMINDAHAN CACHE #####
def move_pycache_to_bin():
    src_pycache = './src/__pycache__'
    dest_bin = './bin'

    # Cek apakah __pycache__ ada
    if os.path.exists(src_pycache):
        # Kalau belum ada folder bin, buat folder bin
        if not os.path.exists(dest_bin):
            os.makedirs(dest_bin)
        
        # Pindahkan semua file di __pycache__ ke bin
        for filename in os.listdir(src_pycache):
            src_file = os.path.join(src_pycache, filename)
            dest_file = os.path.join(dest_bin, filename)
            # Move file
            shutil.move(src_file, dest_file)
        
        # Hapus folder __pycache__
        os.rmdir(src_pycache)