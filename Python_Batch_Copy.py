import os
import shutil

def copy_files(source_folder, destination_folder):
    # Check if the source folder exists
    if not os.path.isdir(source_folder):
        print(f"Error: Source folder '{source_folder}' does not exist.")
        return

    # Check if the destination folder exists; if not, create it
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Get the list of files in the source folder
    files_list = os.listdir(source_folder)

    # Copy each file to the destination folder, checking for duplicates
    for file_name in files_list:
        source_file_path = os.path.join(source_folder, file_name)
        destination_file_path = os.path.join(destination_folder, file_name)

        # Check if the file already exists in the destination folder
        if os.path.exists(destination_file_path):
            print(f"Skipping '{file_name}' - File already exists in the destination folder.")
        else:
            shutil.copy2(source_file_path, destination_folder)
            print(f"Successfully copied '{file_name}' to the destination folder.")

# Specify the source and destination folder paths
source_folder = input("Enter the source folder path: ")
destination_folder = input("Enter the destination folder path: ")

# Copy files from the source folder to the destination folder
copy_files(source_folder, destination_folder)
