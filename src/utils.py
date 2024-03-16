import os
import glob
import shutil

##### ALGORITMA UPDATE DIRECTORY #####
def update_num_of_folders():
    global num_of_folders
    output_path = './test/Output/'
    if not os.path.exists(output_path):
        os.makedirs(output_path)
        num_of_folders = 1
    else:
        # List existing directories and find the maximum existing folder number
        folders = glob.glob(output_path + '*/')
        max_num = 0
        for folder in folders:
            folder_name = os.path.basename(os.path.dirname(folder))  
            if folder_name.isdigit():
                max_num = max(max_num, int(folder_name))
        num_of_folders = max_num + 1  


##### ALGORITMA PEMINDAHAN CACHE #####
src_pycache = './src/__pycache__'
dest_bin = './bin'

# Pindahkan isi __pycache__ ke bin
def move_pycache_to_bin():
    # Check if __pycache__ exists in the src directory
    if os.path.exists(src_pycache):
        # Check if bin directory exists, if not create it
        if not os.path.exists(dest_bin):
            os.makedirs(dest_bin)
        
        # Move each file in the __pycache__ directory
        for filename in os.listdir(src_pycache):
            src_file = os.path.join(src_pycache, filename)
            dest_file = os.path.join(dest_bin, filename)
            # Move file
            shutil.move(src_file, dest_file)
        
        # Remove the now empty __pycache__ directory
        os.rmdir(src_pycache)