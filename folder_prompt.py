import tkinter as tk
from tkinter.filedialog import askdirectory
import os

root = tk.Tk()
root.withdraw()

while True:
    path = askdirectory(title='Select a folder')

    if path:
        if not os.listdir(path):
            print("The folder is empty. Please select a non-empty folder.")
        else:
            files = os.listdir(path)
            print(f"Folder selected: {path}")

            tif_files = []
            other_files = []

            total_tif_size = 0

            for filename in os.listdir(path):
                full_path = os.path.join(path, filename)

                if os.path.isfile(full_path):
                    if filename.lower().endswith(('.tif', '.tiff')):
                        tif_files.append(filename)
                        total_tif_size += os.path.getsize(full_path)
                    else:
                        other_files.append(filename)

            if len(tif_files) > 0:
                print(f"Number of TIF files found: {len(tif_files)}")
                print(f"Total size of TIF files: {total_tif_size / (1024 * 1024):.2f} MB")
            else:
                print("No TIF files found.")

            print(f"Number of non-TIF files found: {len(other_files)}")
            break
    else:
        print("No folder selected. Exiting the program.")
        break