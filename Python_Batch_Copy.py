import os
import shutil
import tkinter as tk
from tkinter import filedialog

def select_source_folder():
    source_folder = filedialog.askdirectory()
    source_entry.delete(0, tk.END)
    source_entry.insert(0, source_folder)

def select_destination_folder():
    destination_folder = filedialog.askdirectory()
    destination_entry.delete(0, tk.END)
    destination_entry.insert(0, destination_folder)

def copy_files():
    source_folder = source_entry.get()
    destination_folder = destination_entry.get()

    # Check if the source folder exists
    if not os.path.isdir(source_folder):
        result_label.config(text=f"Error: Source folder '{source_folder}' does not exist.")
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
            result_label.config(text=f"Skipping '{file_name}' - File already exists in the destination folder.")
        else:
            shutil.copy2(source_file_path, destination_folder)
            result_label.config(text=f"Successfully copied '{file_name}' to the destination folder.")

# Create the GUI window
root = tk.Tk()
root.title("File Copy GUI")

# Create and place widgets in the window
source_label = tk.Label(root, text="Source Folder:")
source_label.pack()
source_entry = tk.Entry(root)
source_entry.pack()

browse_source_button = tk.Button(root, text="Browse", command=select_source_folder)
browse_source_button.pack()

destination_label = tk.Label(root, text="Destination Folder:")
destination_label.pack()
destination_entry = tk.Entry(root)
destination_entry.pack()

browse_destination_button = tk.Button(root, text="Browse", command=select_destination_folder)
browse_destination_button.pack()

copy_button = tk.Button(root, text="Copy Files", command=copy_files)
copy_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Run the GUI
root.mainloop()

