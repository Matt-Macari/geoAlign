###################################################################################
# Developed by Matthew Marcotullio, Matt Macari, Lily Yassemi, and Dylan Lucas    #
#             for California State Polytechnic University, Humboldt               #
###################################################################################
from tkinter.filedialog import askdirectory
import tkinter as tk
import os
os.environ['PYTHONWARNINGS'] = 'ignore::UserWarning'
os.environ['NO_IMK_CLIENT'] = '1'  # Disables IMKClient messages


# Hide the Tkinter root window
root = tk.Tk()
root.withdraw()

# Prompts user to select a folder
# Prints properties of folder user selects
# Returns path for folder user selects
# Returns "exit" if selection is cancled
def select_input_folder():
    while True:
        path = askdirectory(title='Select input directory')

        if not path:
            print("No folder selected. Exiting the program.")
            return "exit", 0

        print(f"\nSelected input directory: {path}\n")

        # Convert absolute path to relative
        path = os.path.relpath(path)

        # Check if the directory is empty
        if not os.listdir(path):
            print("The selected folder is empty. Please select a different folder.\n")
            continue

        tif_files = []
        other_files = []
        total_tif_size = 0

        for filename in os.listdir(path):
            full_path = os.path.join(path, filename)

            if os.path.isfile(full_path):
                if filename.lower().endswith(('.tif', '.tiff')):
                    tif_files.append(filename)
                    total_tif_size += os.path.getsize(full_path)
                elif filename != '.DS_Store':
                    other_files.append(filename)

        num_tif_files = len(tif_files)

        if num_tif_files > 0:
            print('Input directory statistics:')
            print(f"Number of TIFF files: {num_tif_files}")

            # Check if size is 1 GB or more and display accordingly
            total_size_gb = total_tif_size / (1024 * 1024 * 1024)
            if total_size_gb >= 1:
                print(f"Total size of all TIFF files: {total_size_gb:.2f} GB")
            else:
                total_size_mb = total_tif_size / (1024 * 1024)
                print(f"Total size of all TIFF files: {total_size_mb:.2f} MB")
            
            if len(other_files) > 0:
                print(f"Number of non-TIFF files found: {len(other_files)}")
            return path, num_tif_files
        else:
            print("No TIFF files found in the selected folder. Please select a different folder.\n")

# Prompts user to select a folder
# Returns path for folder user selects
# Returns "exit" if selection is cancled
def select_output_folder():
    while True:
            # Step 2: Ask user to select the second folder (output folder)
            #print()
            #print('Select output directory')
            path = askdirectory(
                title='Select output directory')
            if path:
                # Step 3: Loop through each TIFF file and create a text file in the output directory
                print(f"\nSelected output directory: {path}\n")
                print('-----------------------\n')
                return path
            else:
                print("No folder selected. Exiting the program.")
                return "exit"